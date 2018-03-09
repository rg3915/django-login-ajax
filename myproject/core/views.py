from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import LoginForm


def index(request):
    form = LoginForm()
    if request.is_ajax() and request.method == 'POST':
        form = LoginForm(request, request.POST)
        user = None
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response = {'status': 'logged'}
            return JsonResponse(response)
        else:
            response = {'status': 'error'}
            return JsonResponse(response)
            # return HttpResponse('Usuário inválido')
    ctx = {'form': form}
    return render(request, 'index.html', ctx)
