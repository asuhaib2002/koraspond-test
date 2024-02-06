from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload', views.ExcelUploadView.as_view(), name='upload'),
    path('upload/success', views.upload_success, name='upload-success'),
    path('categories/', views.CategoriesListView.as_view(), name='categories'),
    path('categories/<int:category_id>/', views.ProductsByCategoryListView.as_view(), name='products_by_category'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]