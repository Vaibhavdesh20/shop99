from django.urls import path 
from .views import ProductList , ProductDetail , BrandList , BrandDetail


urlpatterns = [
    path('' , ProductList.as_view()),
    path('<int:id>' , ProductDetail.as_view()),
    path('brands' , BrandList.as_view()),
    path('brands/<slug:slug>' , BrandDetail.as_view()),
]
