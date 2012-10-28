from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

def accounts(request):
    page = "Accounts"
    # emulations = ExtendedFlatPage.objects.all()
    return render_to_response('login.html', {'page' : page}, context_instance=RequestContext(request))

