from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='photo_images',
        verbose_name='Image',
    )
    title = models.CharField(max_length=100, verbose_name='Title')
    author = models.ForeignKey(
        to=get_user_model(),
        related_name='photos',
        on_delete=models.CASCADE,
        verbose_name='Author',
    )
    bookmarked_users = models.ManyToManyField(
        to=get_user_model(),
        related_name='bookmarked_photos',
        through='gallery.Bookmark',
        through_fields=('photo', 'user'),
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')

    def __str__(self):
        return "{}. {} by {}".format(self.pk, self.title, self.author)


class Bookmark(models.Model):
    photo = models.ForeignKey(
        to='gallery.Photo', on_delete=models.CASCADE,
        related_name='photo_bookmarks', verbose_name='Photo'
    )
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE,
        verbose_name='User', related_name='user_bookmarks'
    )

    class Meta:
        unique_together = ['user', 'photo']

    def __str__(self):
        return f'{self.user} bookmarks photo "{self.photo}"'
