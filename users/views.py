from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, \
    RetrieveUpdateAPIView
from users.serializers import UserSerializer
from users.models import User
from rest_framework import permissions, status
from rest_framework.response import Response


class UserCreateAPIView(CreateAPIView):
    """
    Класс создания пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()


class UserUpdateAPIView(UpdateAPIView):
    """
    Класс редактирования пользователя. Админом.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated, IsModeratorOrOwner]


class UserDestroyAPIView(DestroyAPIView):
    """
    Класс для удаления пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated, IsModeratorOrOwner]


class UserListAPIView(ListAPIView):
    """
    Класс для просмотра списка пользователей
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserRetrieveAPIView(RetrieveAPIView):
    """
    Класс для просмотра одного пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated, IsModeratorOrOwner]


class UserProfileUpdateAPIView(RetrieveUpdateAPIView):
    """
    Обновление профиля пользователя.
    """
    serializer_class = UserSerializer

    # permission_classes = [permissions.IsAuthenticated]  # Требуется аутентификация

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        if self.get_object() != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
