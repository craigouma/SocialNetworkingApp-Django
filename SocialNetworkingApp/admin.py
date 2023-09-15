from django.contrib import admin
from .models import UserProfile, Post, Comment, Like


# Register the UserProfile model to appear in the admin interface
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    list_filter = ('user',)
    search_fields = ('user__username', 'bio')


# Register the Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('author__username', 'content')


# Register the Comment model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created_at')
    list_filter = ('post', 'author', 'created_at')
    search_fields = ('post__author__username', 'text')


# Register the Like model
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')
    list_filter = ('post', 'user')
    search_fields = ('post__author__username',)
