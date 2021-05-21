from .models import *
import pandas as pd


def do():
    
    file_name = 'data.xls'
    df = pd.read_excel(file_name, sheet_name=None)
    df['Schools'] = df['Schools'].fillna('')
    df['Books'] = df['Books'].fillna('')
    df['Students'] = df['Students'].fillna('')

    idx = df['Schools'].columns


    for i in range(len(df['Schools'])):
        School.objects.create(
            school_name = df['Schools'][idx[1]][i],
            email = df['Schools'][idx[2]][i],
            principal = df['Schools'][idx[3]][i],
            phone_no = df['Schools'][idx[4]][i],
            address = df['Schools'][idx[5]][i]
        ) 

    idx = df['Books'].columns

    for i in range(len(df['Books'])):
        if isinstance(df['Books'][idx[2]][i],str):
            Book.objects.create(
                title = df['Books'][idx[0]][i],
                author_name = df['Books'][idx[1]][i],
                pages = df['Books'][idx[3]][i])
        else:
            Book.objects.create(
                title = df['Books'][idx[0]][i],
                author_name = df['Books'][idx[1]][i],
                date_of_publication = df['Books'][idx[2]][i],
                pages = df['Books'][idx[3]][i])

    idx = df['Students'].columns

    for i in range(len(df['Students'])):
        Student.objects.create(
            sid = df['Students'][idx[0]][i],
            first_name = df['Students'][idx[1]][i],
            last_name = df['Students'][idx[2]][i],
            email = df['Students'][idx[3]][i],
            gender = df['Students'][idx[4]][i]
        )

        obj1 =  Student.objects.get(sid = df['Students'][idx[0]][i])
        Reading.objects.create(student = obj1)

        if df['Students'][idx[6]][i] != '':
            obj2 = Book.objects.get(title = df['Students'][idx[6]][i])
            Reading.objects.filter(pk = obj1.pk).update(book = obj2)
        
        if df['Students'][idx[5]][i] != '':
            obj3 = School.objects.get(school_name = df['Students'][idx[5]][i])
            Reading.objects.filter(pk = obj1.pk).update(school = obj3)


