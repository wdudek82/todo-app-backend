from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from .permissions import IsAuthorOrReadOnly


# TODO: Need testing (especially custom permissions)
class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def pre_save(self, obj):
        obj.user = self.request.user
