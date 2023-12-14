from django.urls import path
from apps.chat.views import whatsapp_webhook

urlpatterns = [
    path('whatsapp-webhook/', whatsapp_webhook, name='whatsapp_webhook'),
]