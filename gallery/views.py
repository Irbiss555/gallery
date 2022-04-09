from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'gallery/photo/photo_update.html'
    model = Photo
    form_class = PhotoForm
    permission_required = 'gallery.change_photo'

    def get_success_url(self):
        return reverse('gallery:photo_detail', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

#
# class ProductDeleteView(PermissionRequiredMixin, DeleteView):
#     model = Product
#     permission_required = 'market.add_product'
#
#     def get_success_url(self):
#         return reverse('market:product_list')