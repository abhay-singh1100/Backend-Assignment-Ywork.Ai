from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer

# Create your views here.

class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user)
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
