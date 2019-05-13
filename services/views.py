from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class DashboardView(TemplateView):
    """docstring for DashboardView"""
    template_name='services/dashboard.html'
