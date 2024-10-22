from django.urls import path
from .views import AdvertDetail, AdvertCreate, AdvertUpdate, AdvertDelete

urlpatterns = [
    path('<int:pk>/', AdvertDetail.as_view(), name='advert_detail'),
    path('create/', AdvertCreate.as_view(), name='advert_create'),
    path('<int:pk>/edit/', AdvertUpdate.as_view(), name='advert_edit'),
    path('<int:pk>/delete/', AdvertDelete.as_view(), name='advert_delete'),
]
