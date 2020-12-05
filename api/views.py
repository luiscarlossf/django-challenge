from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RegularPlanSerializer
from .models import RegularPlan

class RegularPlanViewset(viewsets.ModelViewSet):
    queryset = RegularPlan.objects.all()
    serializer_class = RegularPlanSerializer
