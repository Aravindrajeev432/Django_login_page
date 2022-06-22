from django.contrib import admin
from .models import user
# Register your models here.

class users(admin.ModelAdmin):
    list_display = ('username','password')

admin.site.register(user,users)