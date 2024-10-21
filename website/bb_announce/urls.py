from django.urls import path
from .views import AdvertDetail


urlpatterns = [
    path('<int:pk>/', AdvertDetail.as_view(), name='advert_detail'),
]
