import simplejson as json
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

def accounts(request):
    page = "Accounts"
    # emulations = ExtendedFlatPage.objects.all()
    return render_to_response('login.html', {'page' : page}, context_instance=RequestContext(request))

# errors:
# EMAIL email isn't tied to account
# PASSWORD password isn't correct

def signin(request):
    response = {}
    response['success'] = False
    response['errors'] = {}
    args = json.loads(request.POST.get('data'))
    username =  args['email'].lower()
    password = args['password']
    if (len(User.objects.filter(username=username)) < 1):
        response['errors']['EMAIL'] = True
        # email doesn't exist
        return HttpResponse(json.dumps(response), mimetype='application/json')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            response['success'] = True
            # success!
            return HttpResponse(json.dumps(response), mimetype='application/json')
    # password didn't match
    response['errors']['PASSWORD'] = True
    return HttpResponse(json.dumps(response), mimetype='application/json')

# errors:
# EMAIL email isn't a valid email
# EMAIL_EXISTS email is already tied to an account
# PASSWORD password isn't right size
# PASSWORD_REPEAT passwords didn't match

def signup(request):
    response = {}
    response['success'] = False
    response['errors'] = {}
    args = json.loads(request.POST.get('data'))
    username =  args['email'].lower()
    password = args['password']
    print password
    password_repeat = args['password_repeat']
    f = forms.EmailField()
    try:
        f.clean(username)
    except:
        response['errors']['EMAIL'] = True
        # email isn't email
        return HttpResponse(json.dumps(response), mimetype='application/json')
    if (len(User.objects.filter(username=username)) > 0):
        response['errors']['EMAIL_EXISTS'] = True
        # email already tied to an account
        return HttpResponse(json.dumps(response), mimetype='application/json')
    if (len(password) < 6 or len(password) > 12):
        response['errors']['PASSWORD'] = True
        # password isn't right size
        return HttpResponse(json.dumps(response), mimetype='application/json')
    if (password != password_repeat):
        response['errors']['PASSWORD_REPEAT'] = True
        return HttpResponse(json.dumps(response), mimetype='application/json')
    response['success'] = True
    user = User.objects.create_user(username=username, email=username, password=password)
    user.save()
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            response['success'] = True
            # success!
            return HttpResponse(json.dumps(response), mimetype='application/json')

def signout(request):
    logout(request)
    return redirect('/accounts/')