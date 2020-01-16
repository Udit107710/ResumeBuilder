from django.urls import path
from .views import ResumeList

urlpatterns = [
    path("resumes", ResumeList.as_view(), name="list-resumes")
]