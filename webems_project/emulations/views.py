from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

def mine(request):
    page = "My Emulations"
    emulations = ""
    return render_to_response('emulations.html', {'emulations' : emulations, 'page' : page}, context_instance=RequestContext(request))

def all(request):
    page = "All Emulations"
    emulations = ""
    return render_to_response('emulations.html', {'emulations' : emulations, 'page' : page}, context_instance=RequestContext(request))

def create(request):
    page = "Create"
    return render_to_response('create.html', {'page' : page}, context_instance=RequestContext(request))

def edit(request):
    page = "edit"
    return render_to_response('create.html', {}, context_instance=RequestContext(request))
