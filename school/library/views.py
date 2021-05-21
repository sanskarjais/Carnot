from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q 
from django.views.generic import ListView
from .filters import StudentFilter

from .populate import do
from .models import *
import pandas as pd

populate = False


def HomeView(request):
        
    if populate:
        do()
    return render(request, 'home.html')


def search(request):
    student_list = Student.objects.all()
    student_filter = StudentFilter(request.GET, queryset = student_list)
    final = {'filter':student_filter}
    try:
        num = student_filter.qs[0].sid
        obj = Reading.objects.get(student= num)
        # When there are students who read more than one book.
        # print(Reading.objects.filter(student = num)) 
        final['stud'] = student_filter.qs[0]
        final['boo'] = obj  
        final['pg'] = Book.objects.get(title = obj.book)

    except:
        pass

    return render(request, 'results.html', final)


def student(request, sid):
    dic = {}
    obj = Student.objects.get(sid = sid) 
    dic['obj'] = obj
    try:
        obj1 = Reading.objects.get(student = sid)
        dic['school'] = obj1.school
        dic['book'] = obj1.book
        dic['pages'] = Book.objects.get(title = obj1.book)
        print(obj1.book)
    except:
        pass
  
    return render(request, 'student.html', dic) 
