from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .serializer import StudentSerializer,TeacherSerializer
from .models import *
# Create your views here.

@api_view(['POST'])
def postStudent(request):
    try:
        request_data = request.data
        serialized_data = StudentSerializer(data= request_data, many= False)
        if serialized_data.is_valid(raise_exception= True):
            serialized_data.save()
            return Response({'Message': 'Student Added Successfully..'})
    except Exception as e:
        return Response({'err': e})

@api_view(['POST'])
def postTeacher(request):
    try:
        request_data = request.data
        serialized_data = TeacherSerializer(data= request_data, many= False)
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response({'Message': 'Teacher Added Successfully..'})
    except Exception as e:
        return Response({'err': e})

@api_view(['GET'])
def getStudent(request):
    try:
        students = Student.objects.all()
        serialized_data = StudentSerializer(students, many=True)
        return Response(serialized_data.data)
    except Exception as e:
        return Response({"err": e})

@api_view(['GET'])
def getStudentId(request,id):
    try:
        students = Student.objects.get(id=id)
        serialized_data = StudentSerializer(students, many=False)
        return Response(serialized_data.data)
    except Exception as e:
        return Response({"err": e})

@api_view(['GET'])
def getTeacher(request):
    try:
        teachers = Teacher.objects.all()
        serialized_data = TeacherSerializer(teachers, many=True)
        return Response(serialized_data.data)
    except Exception as e:
        return Response({"err": e})

@api_view(['GET'])
def getTeacherId(request,id):
    try:
        teachers = Teacher.objects.get(id=id)
        serialized_data = TeacherSerializer(teachers, many=False)
        return Response(serialized_data.data)
    except Exception as e:
        return Response({"err": e})

@api_view(['POST'])
def editStudentData(request, id):
    student = Student.objects.get(id=id)
    serialized_data = StudentSerializer(student, data=request.data, many=False, partial=True)
    try:
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response({"Message": "Student Data Updated Successfully"})
    except Exception as e:
        return Response({"err": e})

@api_view(['POST'])
def editTeacherData(request, id):
    teacher = Teacher.objects.get(id=id)
    serialized_data = TeacherSerializer(teacher, data=request.data, many=False, partial=True)
    try:
        if serialized_data.is_valid(raise_exception=True):
            serialized_data.save()
            return Response({"Message": "Teacher Data Updated Successfully"})
    except Exception as e:
        return Response({"err": e})

@api_view(['GET'])
def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response({"Message": "Student deleted successfully"})

@api_view(['GET'])
def deleteTeacher(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return Response({"Message": "Teacher deleted successfully"})