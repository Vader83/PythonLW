from django.contrib import admin

from .models import User
from .models import News

admin.site.register(User)
admin.site.register(News)
