import os
import requests
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import login
from django.http import JsonResponse, HttpResponseBadRequest
from dotenv import load_dotenv
from .oauth_models import UserSocialAuth

load_dotenv()

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
GOOGLE_REDIRECT_URI = os.getenv('GOOGLE_REDIRECT_URI')

SCOPE = 'openid email profile'

def google_login(request):
    oauth_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?"
        f"client_id={GOOGLE_CLIENT_ID}&"
        f"redirect_uri={GOOGLE_REDIRECT_URI}&"
        f"response_type=code&"
        f"scope={SCOPE}&"
        f"access_type=offline&"
        f"prompt=consent"
    )
    return redirect(oauth_url)

def google_callback(request):
    code = request.GET.get('code')
    if not code:
        return HttpResponseBadRequest('Missing code parameter')

    # Exchange code for tokens
    token_url = 'https://oauth2.googleapis.com/token'
    data = {
        'code': code,
        'client_id': GOOGLE_CLIENT_ID,
        'client_secret': GOOGLE_CLIENT_SECRET,
        'redirect_uri': GOOGLE_REDIRECT_URI,
        'grant_type': 'authorization_code',
    }
    r = requests.post(token_url, data=data)
    if r.status_code != 200:
        return HttpResponseBadRequest('Failed to obtain tokens')
    tokens = r.json()
    access_token = tokens['access_token']
    refresh_token = tokens.get('refresh_token')
    expires_in = tokens.get('expires_in')
    token_expiry = timezone.now() + timezone.timedelta(seconds=expires_in)

    # Get user info
    userinfo_url = 'https://www.googleapis.com/oauth2/v2/userinfo'
    headers = {'Authorization': f'Bearer {access_token}'}
    userinfo_resp = requests.get(userinfo_url, headers=headers)
    if userinfo_resp.status_code != 200:
        return HttpResponseBadRequest('Failed to obtain user info')
    userinfo = userinfo_resp.json()
    email = userinfo['email']
    username = email.split('@')[0]

    # Get or create user
    user, created = User.objects.get_or_create(username=username, defaults={'email': email})
    if created:
        user.set_unusable_password()
        user.save()

    # Store tokens
    UserSocialAuth.objects.update_or_create(
        user=user,
        defaults={
            'access_token': access_token,
            'refresh_token': refresh_token or '',
            'token_expiry': token_expiry,
        }
    )

    login(request, user)
    return JsonResponse({'message': 'Authentication successful', 'username': user.username, 'email': user.email})