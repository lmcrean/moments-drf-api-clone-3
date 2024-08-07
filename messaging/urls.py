# drf_api/messaging/urls.py

from django.urls import path
from .views import MessageListView, MessageDetailView, MessageDetailSendView, MessageListStartNewView, MessageDeleteView

urlpatterns = [
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('messages/<int:user_id>/', MessageDetailView.as_view(), name='message-detail'),
    path('messages/<int:user_id>/send/', MessageDetailSendView.as_view(), name='message-detail-send'),
    path('messages/<int:user_id>/start/', MessageListStartNewView.as_view(), name='message-start-new'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message-delete'),
]