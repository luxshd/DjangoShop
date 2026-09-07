from idlelib import query

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView
from store.models import Book


class BookDetailView(DetailView):
    model = Book
    template_name = "store/book_detail.html"
    context_object_name = "book"


class BookListView(ListView):
    model = Book
    template_name = "store/books_list.html"
    context_object_name = "books"
    paginate_by = 3

    def get_queryset(self):
        queryset = Book.objects.select_related('category').all()

        # Поиск по титулу товара
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))



        return queryset

