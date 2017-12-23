from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import LoginForm


def index(request):
    form = LoginForm()
    if request.is_ajax() and request.method == 'POST':
        username = request.POST.get('id_username')
        password = request.POST.get('id_password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = {'status': 'logged'}
            return JsonResponse(response)
        else:
            return HttpResponse('Usuário inválido')
        # form = LoginForm(request.POST)
        # if form.is_valid():
        #     user = authenticate(username=username, password=password)
    ctx = {'form': form}
    return render(request, 'index.html', ctx)
