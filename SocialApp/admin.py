from django.contrib import admin
from .models import News, Comment

class NewsAdmin(admin.ModelAdmin):
	list_display = ('subject', 'user', 'text')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'news', 'comment')

admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)

