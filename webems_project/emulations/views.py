from models import ExtendedFlatPage, MyEmulations
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

def mine(request):
    page = "My Emulations"
    emulations = ExtendedFlatPage.objects.all().filter(created_by=request.user.id)
    return render_to_response('emulations.html', {'emulations' : emulations, 'page' : page}, context_instance=RequestContext(request))

def all(request):
    page = "All Emulations"
    emulations = ExtendedFlatPage.objects.all()
    return render_to_response('emulations.html', {'emulations' : emulations, 'page' : page}, context_instance=RequestContext(request))

def create(request):
    page = "Create"
    return render_to_response('create.html', {'page' : page}, context_instance=RequestContext(request))

def view(request, pk, url=""):
    content = "Emulation " + pk + "does not exist. <a href='/''>Home</a>."
    try:
        f = ExtendedFlatPage.objects.get(id=pk)
        content = f.content
    except ExtendedFlatPage.DoesNotExist:
        pass
    except ExtendedFlatPage.MultipleObjectsReturned:
        pass
    return render_to_response('emulation.html', {'content' : content})

def edit(request, pk, url=""):
    content = "Emulation " + pk + "does not exist. <a href='/''>Home</a>."
    try:
        f = ExtendedFlatPage.objects.get(id=pk)
        content = f.content
    except ExtendedFlatPage.DoesNotExist:
        pass
    except ExtendedFlatPage.MultipleObjectsReturned:
        pass
    return render_to_response('emulation.html', {'content' : content})

def delete(request, pk, url=""):
    content = "Emulation " + pk + "does not exist. <a href='/''>Home</a>."
    try:
        f = ExtendedFlatPage.objects.get(id=pk)
        content = f.content
    except ExtendedFlatPage.DoesNotExist:
        pass
    except ExtendedFlatPage.MultipleObjectsReturned:
        pass
    return render_to_response('emulation.html', {'content' : content})

def myemulations(request, pk, url=""):
    content = "Emulation " + pk + "does not exist. <a href='/''>Home</a>."
    try:
        f = ExtendedFlatPage.objects.get(id=pk)
        content = f.content
    except ExtendedFlatPage.DoesNotExist:
        pass
    except ExtendedFlatPage.MultipleObjectsReturned:
        pass
    return render_to_response('emulation.html', {'content' : content})
