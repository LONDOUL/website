from django.http import JsonResponse
from django.shortcuts import render
from student.models import Student


def index(request, id_student=None):
    if id_student is not None:
        try:
            student_by_id = Student.objects.get(id=id_student)
            return render(request, "student/index_db.html", context={"student": student_by_id})
        except Student.DoesNotExist:
            return render(request, "student/index_not_found.html")
    students = Student.objects.all()
    return render(request, "student/index_db_all.html", context={"students": students})


# def index(request):
#     data = {
#         'responsable': True,
#         'nom': 'Almamy',
#         'notes': {
#             'stats': 10,
#             'IA': 17,
#             'Python': 18
#         },
#         'cours': [
#             'Django',
#             'PHP',
#             'Python',
#             'JavaScript'
#         ]
#     }
#     return render(request, 'student/index.html', data)
def student(request, name=None):
    if name is None:
        return render(request, "student/student.html", context={"name": "les étudiants"})
    return render(request, "student/student.html", context={"name": name})


def student_db(request, id_student=None):
    if id_student is not None:
        try:
            student_by_id = Student.objects.get(id=id_student)
            student_data = {
                'lastname': student_by_id.lastname,
                'firstname': student_by_id.firstname,
                'classe': student_by_id.classe,
            }
            return render(request, "student/student_db.html", context={"student": student_by_id, "students_json": JsonResponse(student_data).content.decode('utf-8')})
        except Student.DoesNotExist:
            return render(request, "student/student_not_found.html")
    students = Student.objects.all()
    students_list = []

    for student in students:
        student_dict = {
            'lastname': student.lastname,
            'firstname': student.firstname,
            'classe': student.classe,
        }
        students_list.append(student_dict)
    return render(request, "student/student_db_all.html", context={"students": students, "students_json": JsonResponse(students_list, safe=False).content.decode('utf-8')})


def student_db_json(request, id_student=None):
    if id_student is not None:
        try:
            student_by_id = Student.objects.get(id=id_student)
            student_dict = {
                'lastname': student_by_id.lastname,
                'firstname': student_by_id.firstname,
                'classe': student_by_id.classe,
            }
            return JsonResponse(student_dict)
        except Student.DoesNotExist:
            return render(request, "student/student_not_found.html")
    students = Student.objects.all()
    students_list = []

    for student in students:
        student_dict = {
            'lastname': student.lastname,
            'firstname': student.firstname,
            'classe': student.classe,
        }
        students_list.append(student_dict)
    return JsonResponse(students_list, safe=False)



# Désérialisation des données JSON en une liste d'objets Python
# students = json.loads(data_json)