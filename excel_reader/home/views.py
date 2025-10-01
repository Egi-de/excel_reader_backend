from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import UserSerializer, ExcelDataSerializer
from .models import ExcelData
import traceback

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

from rest_framework.response import Response

class ExcelDataUploadView(generics.CreateAPIView):
    serializer_class = ExcelDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data_list = request.data.get('data', [])
        user = request.user
        created_objects = []
        for item in data_list:
            serializer = self.get_serializer(data={
                'user': user.id,
                'title': item.get('title'),
                'description': item.get('description'),
                'location': item.get('location'),
                'date': item.get('date'),
            })
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            created_objects.append(serializer.data)
        return Response(created_objects, status=201)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

import logging

logger = logging.getLogger(__name__)

class ExcelDataListView(generics.ListAPIView):
    serializer_class = ExcelDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        try:
            user = self.request.user
            if not user or not user.is_authenticated:
                logger.error("Unauthenticated user tried to fetch Excel data.")
                return ExcelData.objects.none()
            queryset = ExcelData.objects.filter(user=user)
            return queryset
        except Exception as e:
           
            tb = traceback.format_exc()
            logger.error(f"Error fetching Excel data list for user {getattr(self.request.user, 'id', 'unknown')}: {e}\n{tb}")
            return ExcelData.objects.none()
