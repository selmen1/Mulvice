from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from rest_framework.generics import ListAPIView
from django.shortcuts 				import get_object_or_404
from services.models import *

from .serializers import *

class data_list(ListAPIView):
    queryset  = Profile.objects.all()
    serializer_class = ProfileSerializer


# from django.shortcuts import get_object_or_404
# from services.models import Profile
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework.views import APIView


# class ProfileDetail(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'pages/profile_list.html'

#     def get(self, request):
#         profile = get_object_or_404(Profile, pk=1)
#         serializer = ProfileSerializer(profile)
#         return Response({'serializer': serializer, 'profile': profile})

#     def post(self, request):
#         profile = get_object_or_404(Profile, pk=1)
#         serializer = ProfileSerializer(profile, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'profile': profile})
#         serializer.save()
#         return redirect('profile')