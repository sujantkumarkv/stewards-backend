from rest_framework import generics
from .models import Steward, WorkStream, Stats
from .serializers import StewardSerializer, WorkStreamSerializer, StatsSerializer


class StewardView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Steward.objects.all()
    serializer_class = StewardSerializer
    lookup_field = 'user__username'


class StewardsView(generics.ListAPIView):

    queryset = Steward.objects.all()
    serializer_class = StewardSerializer


class WorkStreamView(generics.RetrieveUpdateDestroyAPIView):

    queryset = WorkStream.objects.all()
    serializer_class = WorkStreamSerializer
    lookup_field = 'short_name'


class WorkStreamsView(generics.ListAPIView):

    queryset = WorkStream.objects.all()
    serializer_class = WorkStreamSerializer
