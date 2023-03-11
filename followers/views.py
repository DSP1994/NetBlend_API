from rest_framework import generics, permissions
from api_nb.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


# Create your views here.
class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

