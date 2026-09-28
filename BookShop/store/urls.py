from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    # path("books/", books_list, name="books_list",),
    path("", BookListView.as_view(), name="books_list",),
    path("books/<int:pk>", BookDetailView.as_view(), name="book_detail",),
]