from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # Add Student,Teacher Data
    path('add-student/', postStudent),
    path('add-teacher/', postTeacher),

    # Get Student,Teacher Data All at once
    path('get-student/', getStudent),
    path('get-teacher/', getTeacher),

    # Get Student,Teacher data one by one using unique id
    path('get-student/<id>', getStudentId),
    path('get-teacher/<id>', getTeacherId),

    # Update/edit Student/Teacher Data
    path('edit-student/<id>', editStudentData),
    path('edit-teacher/<id>', editTeacherData),

    # Delete Student/teacher
    path('delete-student/<id>', deleteStudent),
    path('delete-teacher/<id>', deleteTeacher),
]