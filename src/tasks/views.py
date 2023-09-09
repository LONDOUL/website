import csv
import json
from django import forms
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from tasks.models import TaskForm, Task, TaskUpdateForm, TaskFilterForm, TaskCombinedFilterForm


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['user']
        password1 = request.POST['pwd']
        password2 = request.POST['pwd2']

        if password1 == password2:
            try:
                data = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
                data.save()
                messages.success(request, 'Votre compte a été créé avec succès.', extra_tags='success')
                return redirect('login')  # Redirigez vers la page de connexion
            except Exception as e:
                # Enregistrez un message d'erreur avec la classe 'danger'
                messages.error(request, 'Une erreur s\'est produite lors de la création de votre compte.', extra_tags='danger')
        else:
            # Enregistrez un message d'erreur avec la classe 'danger' si les mots de passe ne correspondent pas
            messages.error(request, 'Les mots de passe ne correspondent pas.', extra_tags='danger')
    return render(request, 'account/register.html')


def register2(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['user']
        password1 = request.POST['pwd']
        password2 = request.POST['pwd2']

        data = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
        data.save()
    return render(request, 'account/login.html')


def login2(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pwd']
        user = auth.authentificate(username=username, password=password)

        if user is not None:
            auth.login(request.user)
            return render(request, 'account/login.html')

    return render(request, 'account/login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pwd']

        # Utilisez la fonction authenticate pour vérifier les informations d'identification de l'utilisateur
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            # Utilisez la fonction login pour connecter l'utilisateur
            auth.login(request, user)
        return redirect('task-list')
        # return render(request, 'tasks/list.html')

    return render(request, 'account/login.html')


@login_required
def task_list(request):
    user = request.user

    # Traitez le formulaire de filtre s'il a été soumis
    form = TaskCombinedFilterForm(request.GET)
    status_filter = request.GET.get('status')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Commencez par récupérer toutes les tâches de l'utilisateur
    tasks = Task.objects.filter(user=user)

    # Appliquez le filtre de statut
    if status_filter:
        if status_filter == 'completed':
            tasks = tasks.filter(completed=True)
        elif status_filter == 'not_completed':
            tasks = tasks.filter(completed=False)

    # Appliquez le filtre de date de début et de fin
    if start_date and end_date:
        tasks = tasks.filter(created_date__range=[start_date, end_date])

    return render(request, "tasks/list.html", context={"tasks": tasks, "form": form})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Créez la tâche à partir des données du formulaire
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            # messages.success(request, 'La tâche a été créée avec succès.')
            return redirect('task-list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskUpdateForm(instance=task)

    return render(request, 'tasks/task_update.html', {'form': form, 'task': task})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task-list')


@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Liste des tâches.csv"'

    tasks = Task.objects.filter(user=request.user).order_by('created_date')

    # Traitez le formulaire de filtre s'il a été soumis
    form = TaskCombinedFilterForm(request.GET)
    status_filter = request.GET.get('status')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Appliquez le filtre de statut
    if status_filter:
        if status_filter == 'completed':
            tasks = tasks.filter(completed=True)
        elif status_filter == 'not_completed':
            tasks = tasks.filter(completed=False)

    # Appliquez le filtre de date de début et de fin
    if start_date and end_date:
        tasks = tasks.filter(created_date__range=[start_date, end_date])

    # Créer le writer CSV et écrire les données
    csv_writer = csv.writer(response)
    csv_writer.writerow(['id', 'title', 'description', 'created_date', 'completed'])

    for task in tasks:
        csv_writer.writerow([task.id, task.title, task.description, task.created_date, task.completed])
    return response


@login_required
def export_json(request):
    # Traitez le formulaire de filtre s'il a été soumis
    form = TaskCombinedFilterForm(request.GET)
    status_filter = request.GET.get('status')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Commencez par récupérer toutes les tâches de l'utilisateur
    tasks = Task.objects.filter(user=request.user).order_by('created_date')
    # Appliquez le filtre de statut
    if status_filter:
        if status_filter == 'completed':
            tasks = tasks.filter(completed=True)
        elif status_filter == 'not_completed':
            tasks = tasks.filter(completed=False)

    # Appliquez le filtre de date de début et de fin
    if start_date and end_date:
        tasks = tasks.filter(created_date__range=[start_date, end_date])

    # Convertir les tâches en une liste de dictionnaires
    tasks_data = [{'id': task.id, 'title': task.title, 'description': task.description, 'created_date': task.created_date.strftime('%Y-%m-%d'), 'completed': task.completed} for task in tasks]
    # Générer le JSON en utilisant DjangoJSONEncoder pour gérer les objets 'date'
    data = json.dumps(tasks_data, cls=DjangoJSONEncoder, indent=4)
    response = HttpResponse(data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="Liste des tâches.json"'
    return response


@login_required
def export_json2(request):
    user = request.user
    # Traitez le formulaire de filtre s'il a été soumis
    form = TaskCombinedFilterForm(request.GET)
    status_filter = request.GET.get('status')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Commencez par récupérer toutes les tâches de l'utilisateur
    tasks = Task.objects.filter(user=user)
    # Appliquez le filtre de statut
    if status_filter:
        if status_filter == 'completed':
            tasks = tasks.filter(completed=True)
        elif status_filter == 'not_completed':
            tasks = tasks.filter(completed=False)

    # Appliquez le filtre de date de début et de fin
    if start_date and end_date:
        tasks = tasks.filter(created_date__range=[start_date, end_date])

    # Créez un dictionnaire de données JSON à partir des tâches filtrées
    data = [{'id': task.id, 'title': task.title, 'description': task.description, 'created_date': task.created_date, 'completed': task.completed} for task in tasks]
    return JsonResponse(data, safe=False)


def update_task_2(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_update.html', {'form': form, 'task': task})

