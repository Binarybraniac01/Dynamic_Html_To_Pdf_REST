from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .helper import *

import datetime

class GeneratePdf(APIView):

    # run myapp\faker.py files function in python shell to populate the database
    def get(self, request):
        student_objs = Student.objects.all()
        params = {
            'today' : datetime.date.today(),
            'student_objs' : student_objs
        }
        file_name , status = save_pdf(params)

        if not status :
            return Response({ "status": 403 , "message": "Something went wrong"})

        return Response({ "status": 200, "path": f'/media/{file_name}.pdf' })
