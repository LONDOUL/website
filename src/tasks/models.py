from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'created_date']


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'created_date', 'completed']


class TaskFilterForm(forms.Form):
    status_choices = [
        ('', 'Tous'),  # Option par défaut pour afficher toutes les tâches
        ('completed', 'Terminé'),
        ('not_completed', 'Non terminé'),
    ]
    status = forms.ChoiceField(choices=status_choices, required=False)


class TaskDateFilterForm(forms.Form):
    start_date = forms.DateField(label='Date de début', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end_date = forms.DateField(label='Date de fin', widget=forms.DateInput(attrs={'type': 'date'}), required=False)


class TaskCombinedFilterForm(forms.Form):
    status_choices = [
        ('', 'Tous'),  # Option par défaut pour afficher toutes les tâches
        ('completed', 'Terminé'),
        ('not_completed', 'Non terminé'),
    ]

    status = forms.ChoiceField(choices=status_choices, required=False)
    start_date = forms.DateField(label='Date de début', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end_date = forms.DateField(label='Date de fin', widget=forms.DateInput(attrs={'type': 'date'}), required=False)


class MyForm(forms.Form):
    date_field = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'data-toggle': 'datetimepicker', 'data-target': '#date-picker'}),
        input_formats=['%Y-%m-%d'],
    )


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

