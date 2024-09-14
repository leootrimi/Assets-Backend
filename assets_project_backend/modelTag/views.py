from .models import modelTag
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ModelSerializer
from django.http import JsonResponse
from itertools import groupby
from operator import itemgetter

@csrf_exempt
@api_view(['POST'])
def addModel(request):
    serializer = ModelSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Employer added successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getModel(request):
    model = modelTag.objects.all()
    serializer = ModelSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getByType(request, type):
    print(f"Received request for type: {type}")
    model = modelTag.objects.filter(type__iexact=type)
    if not model.exists():
        return Response({'error': 'Equipment not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ModelSerializer(model, many=True)
    data = serializer.data
    data_sorted = sorted(data, key=itemgetter('model'))

    distinct_models = [next(group) for key, group in groupby(data_sorted, key=itemgetter('model'))]


    return Response(distinct_models)


def getCount(request, model):
    count = modelTag.objects.filter(model__iexact=model).count()
    return JsonResponse({'count': count})