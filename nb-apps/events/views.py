from rest_framework import generics, permissions, filters
from api_nb.permissions import IsOwnerOrReadOnly
from .models import Event


class EventList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()

    filter_backends = [
        filters.SearchFilter,
    ]

    search_fields = [
        'owner__username',
        'title',
        'city',
        'country',
    ]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update & Destroy events.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
