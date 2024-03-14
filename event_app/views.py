from rest_framework import generics
from .models import Organization, Event
from .serializers import OrganizationSerializer, EventSerializer
from rest_framework import permissions
from django.shortcuts import render
from users.models import User

class OrganizationList(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


def event_info(request, pk):
    event = Event.objects.get(id=pk)
    organizations = event.organizations.all()
    members = {key: User.objects.filter(organization=key) for key in organizations}
    return render(request, "index.html", context={"event": event, "members": members})
 