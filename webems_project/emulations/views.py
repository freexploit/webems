import simplejson as json
from emulations.models import ExtendedFlatPage
from accounts.models import MyEmulations
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

def mine(request):
    page = "My Emulations"
    emulations = ""
    me = MyEmulations.objects.all().filter(user=request.user.id)
    if (len(me) > 0):
        emulations = MyEmulations.objects.all().filter(user=request.user.id)[0].emulations.all()
    return render_to_response('emulations.html', {'emulations' : emulations, 'page' : page}, context_instance=RequestContext(request))

def all(request):
    page = "All Emulations"
    emulations = ExtendedFlatPage.objects.all()
    return render_to_response('emulations.html', {'emulations' : emulations, 'page' : page}, context_instance=RequestContext(request))

def create(request):
    page = "Create"
    return render_to_response('create.html', {'page' : page}, context_instance=RequestContext(request))

def view(request, pk):
    content = "Emulation " + pk + "does not exist. <a href='/''>Home</a>."
    try:
        f = ExtendedFlatPage.objects.get(id=pk)
        content = f.content
    except ExtendedFlatPage.DoesNotExist:
        pass
    except ExtendedFlatPage.MultipleObjectsReturned:
        pass
    return render_to_response('emulation.html', {'content' : content})

def edit(request, pk):
    content = "Emulation " + pk + "does not exist. <a href='/''>Home</a>."
    try:
        f = ExtendedFlatPage.objects.get(id=pk)
        content = f.content
    except ExtendedFlatPage.DoesNotExist:
        pass
    except ExtendedFlatPage.MultipleObjectsReturned:
        pass
    return render_to_response('emulation.html', {'content' : content})

def delete(request, pk):
    response = {}
    response['success'] = True
    response['errors'] = {}
    try:
        f = ExtendedFlatPage.objects.get(id=pk)
        f.delete()
    except ExtendedFlatPage.DoesNotExist:
        response['success'] = False
        pass
    except ExtendedFlatPage.MultipleObjectsReturned:
        response['success'] = False
        pass
    return HttpResponse(json.dumps(response), mimetype='application/json')

def myemulations(request, pk):
    response = {}
    response['success'] = True
    response['errors'] = {}
    u = request.user
    try:
        e = ExtendedFlatPage.objects.get(id=pk)
        me = MyEmulations.objects.get(user=u)
        me.emulations.add(e)
        me.save()
    except MyEmulations.DoesNotExist:
        e = ExtendedFlatPage.objects.get(id=pk)
        me = MyEmulations(user=u)
        me.save()
        me.emulations.add(e)
        me.save()
    except ExtendedFlatPage.DoesNotExist:
        response['success'] = False
    except ExtendedFlatPage.MultipleObjectsReturned:
        response['success'] = False
    return HttpResponse(json.dumps(response), mimetype='application/json')

def remove_myemulations(request, pk):
    response = {}
    response['success'] = True
    response['errors'] = {}
    u = request.user
    try:
        e = ExtendedFlatPage.objects.get(id=pk)
    except MyEmulations.DoesNotExist:
        response['success'] = False
    me = MyEmulations.objects.get(user=u)
    if e in me.emulations.all():
        me.emulations.remove(e)
    return HttpResponse(json.dumps(response), mimetype='application/json')