from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from models import ExtendedFlatPage, Rewrites

class ExtendedFlatPageForm(FlatpageForm):
    class Meta:
	    model = ExtendedFlatPage

class ExtendedFlatPageAdmin(FlatPageAdmin):
    form = ExtendedFlatPageForm
    list_display = ('id', 'url', 'title', 'created', 'updated', 'page_url', )
    fieldsets = ( (None, {'fields': ('url', 'title', 'sites', 'created', 'created_by', 'updated', 'updated_by', 'page_url', 'content', 'original_html' )}),)

class RewritesAdmin(admin.ModelAdmin):
	list_display = ('id', 'find', 'replace', 'method')

admin.site.register(Rewrites, RewritesAdmin)
admin.site.unregister(FlatPage)
admin.site.register(ExtendedFlatPage, ExtendedFlatPageAdmin)