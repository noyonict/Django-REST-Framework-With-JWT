from django.shortcuts import render
from rest_framework import viewsets
from .models import Language, Programmer, Paradigm
from .serializers import LanguageSerializers, ParadigmSerializers, ProgrammerSerializers


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializers


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializers


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializers
