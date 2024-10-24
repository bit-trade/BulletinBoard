from django.urls import path
from .views import AdvertDetail, AdvertCreate, AdvertUpdate, AdvertDelete, ReplyCreate, ReplyUpdate, ReplyDelete

urlpatterns = [
    path('<int:pk>/', AdvertDetail.as_view(), name='advert_detail'),
    path('create/', AdvertCreate.as_view(), name='advert_create'),
    path('<int:pk>/edit/', AdvertUpdate.as_view(), name='advert_edit'),
    path('<int:pk>/delete/', AdvertDelete.as_view(), name='advert_delete'),
    path('<int:pk>/reply/create/', ReplyCreate.as_view(), name='reply_create'),
    path('reply/<int:pk>/edit/', ReplyUpdate.as_view(), name='reply_edit'),
    path('reply/<int:pk>/delete/', ReplyDelete.as_view(), name='reply_delete'),
]
