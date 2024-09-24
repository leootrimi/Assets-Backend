from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ESerializer
from .models import EquipmentRequest
from django.http import JsonResponse

@csrf_exempt
@api_view(['POST'])
def addRequest(request):
    serializer = ESerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Employer added successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getRequests(request):
    model = EquipmentRequest.objects.all()
    serializer = ESerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getByStatus(request, status):
    print(f"Received request for id: {status}")
    try:
        reqData = EquipmentRequest.objects.filter(status=status)
    except EquipmentRequest.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ESerializer(reqData, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def approve_request(request, id):
    try:
        request_instance = EquipmentRequest.objects.get(id=id)
    except EquipmentRequest.DoesNotExist:
        return Response({'error': 'Request not found'}, status=status.HTTP_404_NOT_FOUND)
    request_instance.status = 'Approved'
    request_instance.save()

    serializer = ESerializer(request_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def reject_request(request, id):
    try:
        request_instance = EquipmentRequest.objects.get(id=id)
    except EquipmentRequest.DoesNotExist:
        return Response({'error': 'Request not found'}, status=status.HTTP_404_NOT_FOUND)
    request_instance.status = 'Rejected'
    request_instance.save()

    serializer = ESerializer(request_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)