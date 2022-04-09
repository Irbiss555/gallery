from django import forms
from gallery.models import Photo, Bookmark


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'title']


class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        exclude = ['user', 'photo']
