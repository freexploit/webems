from django.contrib import admin
from accounts.models import MyEmulations

class MyEmulationsAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

admin.site.register(MyEmulations, MyEmulationsAdmin)
