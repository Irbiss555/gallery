from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from gallery.forms import PhotoForm
from gallery.models import Photo


class PhotoListView(ListView):
    template_name = 'gallery/photo/photo_list.html'
    model = Photo
    context_object_name = 'photos'


class PhotoDetailView(DetailView):
    template_name = 'gallery/photo/photo_detail.html'
    model = Photo
    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'gallery/photo/photo_create.html'
    model = Photo
    form_class = PhotoForm

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        self.object = photo
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('gallery:photo_detail', kwargs={'pk': self.object.pk})


# class ProductUpdateView(PermissionRequiredMixin, UpdateView):
#     template_name = 'product/product_update.html'
#     model = Product
#     form_class = ProductForm
#     permission_required = 'market.change_product'
#
#     def get_success_url(self):
#         return reverse('detail_product', kwargs={'pk': self.object.pk})
#
#
# class ProductDeleteView(PermissionRequiredMixin, DeleteView):
#     model = Product
#     permission_required = 'market.add_product'
#
#     def get_success_url(self):
#         return reverse('market:product_list')