from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from models import ExtendedFlatPage, MyEmulations, Rewrites


class ExtendedFlatPageForm(FlatpageForm):
    class Meta:
	    model = ExtendedFlatPage
class ExtendedFlatPageAdmin(FlatPageAdmin):
    form = ExtendedFlatPageForm
    list_display = ('id', 'url', 'title', 'created', 'updated', 'page_url', )
    fieldsets = ( (None, {'fields': ('url', 'title', 'sites', 'created', 'updated', 'page_url', 'content', 'original_html' )}),)

class MyEmulationsAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'emulation')

class RewritesAdmin(admin.ModelAdmin):
	list_display = ('id', 'find', 'replace', 'method')

admin.site.register(MyEmulations, MyEmulationsAdmin)
admin.site.register(Rewrites, RewritesAdmin)
admin.site.unregister(FlatPage)
admin.site.register(ExtendedFlatPage, ExtendedFlatPageAdmin)