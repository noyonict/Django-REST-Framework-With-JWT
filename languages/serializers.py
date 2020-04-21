from rest_framework import serializers
from .models import Language, Paradigm, Programmer


class LanguageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['url', 'id', 'name', 'paradigm']


class ParadigmSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ['url', 'id', 'name']


class ProgrammerSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ['url', 'id', 'name', 'languages']