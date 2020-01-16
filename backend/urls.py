from django.urls import path
from .views import ResumeList, Home

urlpatterns = [
    path("resumes", ResumeList.as_view(), name="list-resumes"),
    path("test", Home.as_view(), name="home")
]