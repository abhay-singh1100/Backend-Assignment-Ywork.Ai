from django.contrib import admin
from .models import Order
from .oauth_models import UserSocialAuth

# Register your models here.
admin.site.register(Order)
admin.site.register(UserSocialAuth)
