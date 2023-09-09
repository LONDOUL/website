from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return redirect('task-list')
    else:
        return render(request, 'website/index.html')
    # return render(request, 'website/index.html')


def register(request):
    return render(request, 'account/register.html')


def login(request):
    return render(request, 'account/login.html')