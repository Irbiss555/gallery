from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from gallery.models import Photo, Bookmark


class BookmarkAPIView(APIView):
    photo_obj = None
    permission_classes = [IsAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        self.photo_obj = get_object_or_404(Photo, pk=self.kwargs.get('photo_pk'))
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.request.user in self.photo_obj.bookmarked_users.all():
            self.remove_bookmark()
        else:
            self.add_bookmark()
        response = {'bookmarks_total': self.photo_obj.bookmarked_users.count()}
        return JsonResponse(response, safe=False)

    def remove_bookmark(self):
        bookmark = Bookmark.objects.get(user=self.request.user, photo=self.photo_obj)
        bookmark.delete()

    def add_bookmark(self):
        Bookmark.objects.create(user=self.request.user, photo=self.photo_obj)

