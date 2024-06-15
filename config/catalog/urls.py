from django.urls import path
from .views import (
    BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
    HomeView,
    ContactView,
    ProductDetailView,
    CreateProductView,
    UpdateProductView,
    DeleteProductView,
    CreateVersionView,
    VersionDeleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', CreateProductView.as_view(), name='create_product'),
    path('product/<int:pk>/edit/', UpdateProductView.as_view(), name='update_product'),
    path('product/<int:product_id>/version/<int:pk>/delete/', VersionDeleteView.as_view(), name='delete_version'),
    path('product/<int:pk>/delete/', DeleteProductView.as_view(), name='delete_product'),
    path('blog/new/', BlogPostCreateView.as_view(), name='blog_create'),
    path('blog/', BlogPostListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('blog/<slug:slug>/edit/', BlogPostUpdateView.as_view(), name='blog_update'),
    path('blog/<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='blog_delete'),
    path('version/create/', CreateVersionView.as_view(), name='create_version'),
]
