from django.urls import path
from core.views import FBWebHookView

urlpatterns = [
    path('fb_webhook', FBWebHookView.as_view())
]
