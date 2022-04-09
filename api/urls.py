from django.urls import include, path
from api import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api'

urlpatterns = [
    path('photo/<int:photo_pk>/bookmark/', views.BookmarkAPIView.as_view(), name='bookmark_api'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', obtain_auth_token, name='api_token_auth')
]
