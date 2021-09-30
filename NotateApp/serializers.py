from django.db.models import fields
from rest_framework import serializers
from NotateApp.models import Txt
from NotateApp.models import Tagging


class TxtSerializer (serializers.ModelSerializer):

   class Meta:
       model = Txt
       fields = ('TextId', 'Text')


class TaggingSerializer (serializers.ModelSerializer):

   class Meta:
       model = Tagging
       fields = ('TagId', 'Start', 'Start_span_id',
                 'Txxt', 'End', 'End_span_id', 'Label')
