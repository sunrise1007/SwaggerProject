from rest_framework import generics
from rest_framework.response import Response
from .serializer import PersonSerializer
from .models import Person


class PersonApi(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer