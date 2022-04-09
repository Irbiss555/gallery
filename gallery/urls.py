from django.urls import path
from gallery.views import PhotoListView

app_name = 'gallery'

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list'),
    # path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    # path('product/add', ProductCreateView.as_view(), name='product_create'),
    # path('product/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    # path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    # path('product/<int:pk>/review/create/', ProductReviewCreateView.as_view(), name='product_review_create'),
]
