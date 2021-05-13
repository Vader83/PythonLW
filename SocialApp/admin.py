from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
	list_display = ('subject', 'user', 'text')

admin.site.register(News, NewsAdmin)
