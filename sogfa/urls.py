from .views import BooksViewset, MessagesViewset, download_message, download_book
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from django.urls import path, re_path as url


router = DefaultRouter()
router.register('books', BooksViewset, basename='books')
router.register('messages', MessagesViewset, basename='messages')

urlpatterns = [
    url(r'^', include(router.urls)),
    path('download_message/<int:pk>', download_message),
    path('download_book/<int:pk>', download_book),
]