from django.urls import path

from BookShop import settings
# from .views import books_list, book_detail
from .views import BookListView, BookDetailView

urlpatterns = [
    # path("books/", books_list, name="books_list",),
    path("books/", BookListView.as_view(), name="books_list",),
    path("books/<int:pk>", BookDetailView.as_view(), name="book_detail",),
]