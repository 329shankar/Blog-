from django.contrib import admin
from .models import Post, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')
    search_fields = ['title', 'author__username']
    inlines = [PhotoInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Photo)
