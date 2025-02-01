from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "catalog", "get_tags", "views", "created_at", "updated_at")
    search_fields = ("title", "content", "author__first_name", "author__last_name", "tags__name")
    list_filter = ("created_at", "updated_at", "catalog", "author")
    ordering = ("title", "-created_at")
    fields = ("title", "content", "img", "author", "catalog", "tags", "views")
    readonly_fields = ("created_at", "updated_at", "views")

    def get_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all()) if obj.tags.exists() else "-"

    get_tags.short_description = "Tags"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'short_content', 'email', 'created_at', 'updated_at')
    list_filter = ('created_at', 'post')
    search_fields = ('content', 'author__first_name', 'author__last_name', 'post__title', 'email')
    ordering = ('-created_at',)

    def short_content(self, obj):
        return obj.content[:50] + ("..." if len(obj.content) > 50 else "")

    short_content.short_description = "Comment"
