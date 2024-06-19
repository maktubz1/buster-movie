from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
from users.permissions import IsAuthenticatedUser
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class UserView(APIView):

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class UsersDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAuthenticatedUser]

    def get(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(req, user)

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, req: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(req, user)

        serializer = UserSerializer(user, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
