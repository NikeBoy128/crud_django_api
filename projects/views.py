from django.shortcuts import render
# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from .models import Autos
from .serializers import AutosSerializer
from rest_framework import permissions
from rest_framework import viewsets

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
class ExampleView(APIView):
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  
            'auth': str(request.auth),  
        }
        return Response(content)


class WhoAmIView(APIView):
    def get(self, request):
        user = request.user
        return Response({"username": user.username})

class AutosViewSet(viewsets.ModelViewSet):
    queryset = Autos.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AutosSerializer