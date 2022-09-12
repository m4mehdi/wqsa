from rest_framework import serializers
from web_api import models

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Subject
        fields = '__all__'



class CDNSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.cdnProvider
        fields = '__all__'
        

class QualitySerializer(serializers.Serializer):
    '''serializes a ip field for our APIView'''
    ip = serializers.CharField(max_length = 16)


    
class WebProfileSerializer(serializers.ModelSerializer):
    """serializes a web profile object"""

    class Meta:
        model = models.Site
        fields = '__all__'
    