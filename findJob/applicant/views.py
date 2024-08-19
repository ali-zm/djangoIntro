from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from application.models import Application
from .models import Applicant
from application.serializer import ApplicationSerializer

class applicationPagination(PageNumberPagination):
    page_size = 3

# Create your views here.
class GetApplications(ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    pagination_class = applicationPagination 

class applyForApplication(APIView):    
    def post(self, request):
        applicationID = request.data["app-id"]
        applicantID = request.data["applicant-id"]
        application = Application.objects.get(pk=applicationID)
        applicant = Applicant.objects.get(pk=applicantID)
        application.applicant = applicant
        application.save()
        serializer = ApplicationSerializer(application)
        return Response(serializer.data)
        