from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dat.models import Dat
from dat.serializers import DatSerializer


@api_view(['GET'])
def datApi(request):
    if request.method == 'GET':
        dats = Dat.objects.all()
        serializer = DatSerializer(dats, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def dat_element(request, pk):
    try:
        dat = Dat.objects.get(pk=pk)
    except Dat.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DatSerializer(dat)
        return Response(serializer.data)
