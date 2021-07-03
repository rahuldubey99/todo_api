from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .serializers import PlansSerializer, UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Plans

# Create your views here.


class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {"refresh": str(
                refresh), "access": str(refresh.access_token)}
            return Response(response_data, status=status.HTTP_201_CREATED)
        error = serializer.errors.values()
        return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    def post(self, request, format=None):
        try:
            refresh_token = request.data.get("refresh_token")
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_404_BAD_REQUEST)


class PlansList (ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlansSerializer

    def get_queryset(self):
        queryset = Plans.objects.filter(user=self.request.user)
        return queryset


class PlansCreate(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer


class PlansUpdate(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer


class PlansDestroy (DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer
