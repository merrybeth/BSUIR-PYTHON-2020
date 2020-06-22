from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Publisher, Profile, Mail

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)


# admin.site.register(BookInstance)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'display_publisher')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'date_back', 'id')
    list_filter = ('status', 'date_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'date_back', 'borrower')
        }),
    )


admin.site.register(Author, AuthorAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):                                      #added
    list_display = ['user', 'is_verified']


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('email_caption', 'email_date','email_time')         #added