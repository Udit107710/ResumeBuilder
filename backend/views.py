from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.http import FileResponse

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
import json

from ResumeBuilder.settings import AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
from backend.models import Resume
from backend.forms import ProfileForm

url = "https://"+AWS_STORAGE_BUCKET_NAME+".s3."+AWS_S3_REGION_NAME+".amazonaws.com/"


class ResumeList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        resumes = Resume.objects.all().only('file')
        files = []
        for resume in resumes:
            files.append(url + resume.file.name)
        data = json.dumps({'files': files})
        print(data)
        return Response(data=data, status=HTTP_200_OK, content_type="application/json")


class Home(APIView):

    def get(self, request):
        data = json.dumps({"working": "yes"})
        print(data)
        return Response(data=data, status=HTTP_200_OK, content_type="application/json")


class SendResume(APIView):

    def post(self, request):
        profile = ProfileForm(request.POST)
        if profile.is_valid():
            profile.save()
            data = json.dumps({"email": "successful"})
            resume = Resume.objects.get(file=profile["template"])
            
            return FileResponse(open(resume.file))
        else:
            print(profile.errors)
            return HttpResponse()