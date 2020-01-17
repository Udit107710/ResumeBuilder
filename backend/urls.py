from django.urls import path
from .views import ResumeList, Home, SendResume

urlpatterns = [
    path("resumes", ResumeList.as_view(), name="list-resumes"),
    path("test", Home.as_view(), name="home"),
    path("send-resume/", SendResume.as_view(), name="send-resume")
]