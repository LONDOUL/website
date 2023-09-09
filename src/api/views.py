from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Planet
from api.serializers import StudentSerializer
from student.models import Student
import requests
import pandas as pd


def inserer_et_aff_data(request):
    response = requests.get('https://swapi.dev/api/planets/')
    data = response.json()
    planets_data = data['results']
    for planet_data in planets_data:
        Planet.objects.create(
            name=planet_data['name'],
            rotation_period=planet_data['rotation_period'],
            orbital_period=planet_data['orbital_period'],
            diameter=planet_data['diameter'],
            climate=planet_data['climate'],
            gravity=planet_data['gravity'],
            terrain=planet_data['terrain'],
            surface_water=planet_data['surface_water'],
            population=planet_data['population'],
        )
    planets = Planet.objects.all()
    return render(request, 'api/display_data.html', {'planets': planets})


def planet_list(request):
    url = requests.get('https://swapi.dev/api/planets/')
    df = pd.read_json(url)

    # data = url.json()
    # planets = data['results']
    return render(request, 'api/display_data.html', {'planets': df})


def display_data(request):
    planets = Planet.objects.all()
    return render(request, 'api/display_data.html', {'planets': planets})


# @api_view(['GET', 'POST', 'PUT'])  # Allow GET, POST, and PUT methods
@api_view()
def hello_word(request):
    data = {'message': 'Hello, World!'}
    if request.method == 'POST':
        return Response({'message': f'Hello, World! {request.data}'})
    return Response(data)


class ListStudents(APIView):
    def get(self, request, format=None):
        students = [student for student in Student.objects.all()]
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
        # return render(request, 'student/student_db_all.html', {'students': serializer.data})

    def post(self, request, format=None):
        pass