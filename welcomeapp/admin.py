from django.contrib import admin
from .models import user,Homes
# Register your models here.

class users(admin.ModelAdmin):
    list_display = ('username','password')

admin.site.register(user,users)
class home(admin.ModelAdmin):
    list_display = ('place','price','image')
admin.site.register(Homes,home)