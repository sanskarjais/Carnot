from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length = 100)
    author_name = models.CharField(max_length = 100)
    date_of_publication = models.DateTimeField(blank = True, null = True)
    pages = models.IntegerField(default = 0)


    def __str__(self):
        return self.title
    
class School(models.Model):
    school_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    principal = models.CharField(max_length = 100)
    phone_no = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)

    def __str__(self):
        return self.school_name

class Student(models.Model):
    sid = models.IntegerField()
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email  = models.EmailField(max_length = 100)
    gender = models.CharField(max_length = 100)
    pages_read = models.IntegerField(default = 0)

    def __str__(self):
        
        return self.first_name


class Reading(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete = models.CASCADE, null=True, blank=True)
    school = models.ForeignKey(School, on_delete = models.CASCADE, null = True, blank = True)
    def __str__(self):
        return self.student.first_name
    

