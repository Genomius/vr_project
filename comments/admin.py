from django.contrib import admin
from models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "rating")
    prepopulated_fields = {"slug": ("id", )}


admin.site.register(Comment, CommentAdmin)
