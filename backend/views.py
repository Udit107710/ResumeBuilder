from django.shortcuts import render, HttpResponse
from django.http import FileResponse
from django.core.mail import EmailMessage

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
import json

from ResumeBuilder.settings import AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
from backend.models import Resume
from backend.serializers import ProfileSerializer

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
        return HttpResponse(content=data, status=HTTP_200_OK, content_type="application/json")


class SendResume(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.data)
        profile = ProfileSerializer(data=request.data)
        if profile.is_valid():
            profile.save()
            file = "Resumes/" + profile["template"].value
            resume = Resume.objects.get(file=file)
            email = EmailMessage(
                'Resume',
                'Your resume is ready',
                'uditcr710107@gmail.com',
                [profile["email"].value]
            )
            email.attach('resume.pdf', resume.file.read(), "application/pdf")
            email.send()

            data = json.dumps({"email": "successful", "resume": url+file})
            print(data)
            return Response(data=data, status=HTTP_200_OK, content_type="application/json")
        else:
            print(profile.errors)
            data = json.dumps({"email": "unsuccessful", "resume": ""})
            print(data)
            return Response(data=data, status=HTTP_500_INTERNAL_SERVER_ERROR, content_type="application/json")