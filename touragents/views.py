from rest_framework import generics
from .models import TourAgent
from .serializers import TourAgentSerializer


class TourAgentListCreateView(generics.ListCreateAPIView):
    queryset = TourAgent.objects.all()
    serializer_class = TourAgentSerializer


class TourAgentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TourAgent.objects.all()
    serializer_class = TourAgentSerializer
