from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['title', 'category', 'salary', 'createdTime', 'expirationTime', 'employer', 'applicant']
