from django.contrib import admin

from store.models import Category, Book


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'stock', 'availability', 'created_at', 'updated_at', 'image')
    list_filter = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'author', 'category', 'description')

    @admin.display(
        boolean=True,
        description='availability',
    )
    def availability(self, obj):
        return obj.is_available and obj.stock > 0