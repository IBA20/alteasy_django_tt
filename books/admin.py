from django.contrib import admin

from books.models import Book, Profile


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'author', 'description', 'price')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('column_name',)
    list_display = ('column_name', 'is_visible')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
