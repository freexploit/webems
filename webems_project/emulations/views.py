import simplejson as json
from emulations.models import ExtendedFlatPage
from django.contrib.sites.models import Site
from accounts.models import MyEmulations
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.template import Context, loader

DEBUG_AND_TEST = False
DEBUG_AND_TEST = True

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
    testHTML = ""
    testURL = ""
    if (DEBUG_AND_TEST):
        c = Context({})
        t = loader.get_template('test.html')
        testHTML = t.render(c)
        testURL = "http://google.com/test/"
    return render_to_response('create.html', {'page' : page, 'testHTML' : testHTML, 'testURL' : testURL}, context_instance=RequestContext(request))

def save(request):
    response = {}
    response['success'] = True
    response['errors'] = {}
    u = request.user
    args = json.loads(request.POST.get('data'))
    # 'url' for flatpages needs to be unique :( just want it to be the ID
    pages = ExtendedFlatPage.objects.all().order_by('id')
    url = "0" if len(pages) < 1 else str(pages[len(pages)-1].id+1)
    f = ExtendedFlatPage(page_url=args['url'], content=args['html'], original_html=args['original_html'], title=args['name'], url=url, created_by=u.id, updated_by=u.id)
    f.save()
    f.sites.add(Site.objects.get(id=1))
    f.save()
    response["id"] = f.id
    return HttpResponse(json.dumps(response), mimetype='application/json')

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