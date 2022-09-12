import site
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.views import APIView

from web_api import serializers
from web_api import models
from web_api import permissions
from web_api import QoS

# Create your views here.

class WebProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.WebProfileSerializer
    queryset = models.Site.objects.all()
    permission_classes = (permissions.UpdateProfile,)
    filter_backends = (filters.SearchFilter,) 
    search_fields = ('URL','IP','subject','location','cdn_provider',)


class QualityApiView(APIView):

    serializer_class = serializers.QualitySerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            ip = serializer.validated_data.get('ip')
            delay , jitter = QoS.Delay(ip)
            response_time = QoS.Response(ip)
            s = models.Site.objects.get(IP=ip,)
            try:
                x = models.QualityOfService.objects.get(site=s,)
                x.jitter = jitter
                x.delay = delay
                x.load_time = response_time
            except:
                created = models.QualityOfService(
                    site = s,
                    jitter = jitter,
                    delay = delay,
                    load_time = response_time,
                )
                created.save()
           
            return Response({'Jitter(ms)': jitter, 'Delay(ms)': delay, 'Load Time(ms)': response_time})

