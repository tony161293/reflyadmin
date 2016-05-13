from django.shortcuts import render_to_response
from django.template import RequestContext
from dashboard.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    login_form = loginForm()
    error = ""
    context = RequestContext(request, {'form': login_form, 'error': error})
    if request.method == 'POST':
        login_form = loginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            if authenticate(username=username, password=password).is_active:
                return HttpResponseRedirect('/dashboard')
            else:
                error = "Invalid login credentials"
                context = RequestContext(
                    request, {'form': login_form, 'error': error})
                return render_to_response('login.html',
                                          context_instance=context)
        else:
            error = "Invalid credentials"
            context = RequestContext(
                request, {'form': login_form, 'error': error})
            return render_to_response('login.html',
                                      context_instance=context)
    return render_to_response('login.html',
                              context_instance=context)
