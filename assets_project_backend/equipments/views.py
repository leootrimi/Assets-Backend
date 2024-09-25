from django.db.models import Sum
from django.http import HttpResponse, JsonResponse
from .models import Equipment
from employers.models import Employers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import EquipmentSerializer
@csrf_exempt
@api_view(['POST'])
def addEquipment(request):
    if request.method == 'POST':
        serializer = EquipmentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Equipment added successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getEquipments(request):
    if request.method == 'GET':
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def equipment_detail(request, serial_no):
    print(f"Received request for serial_no: {serial_no}")
    try:
        equipment = Equipment.objects.get(serial_no=serial_no)
    except Equipment.DoesNotExist:
        return Response({'error': 'Equipment not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = EquipmentSerializer(equipment)
    return Response(serializer.data)

@api_view(['GET'])
def count_equipment(request):
    count = Equipment.objects.count()
    return JsonResponse({'count' : count})

@api_view(['GET'])
def total_equipment_price(request):
    total_price = Equipment.objects.aggregate(total_price=Sum('price'))['total_price']
    return JsonResponse({'total_price': total_price})

@api_view(['GET'])
def getCount(request, model):
    count = Equipment.objects.filter(model__iexact=model).count()
    return JsonResponse({'count': count})

@api_view(['GET'])
def getById(request, id):
    try:
        equipment = Equipment.objects.filter(employer=id)
    except Equipment.DoesNotExist:
        return Response({'error': 'Equipment not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = EquipmentSerializer(equipment, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
def updateEquipment(request, serial_no):
    print(f"Received request to update equipment with serial_no: {serial_no}")
    try:
        equipment = Equipment.objects.get(serial_no=serial_no)
    except Equipment.DoesNotExist:
        return Response({'error': 'Equipment not found'}, status=status.HTTP_404_NOT_FOUND)
    data = request.data
    employer_id = data.get('employer')
    if employer_id:
        try:
            employer_instance = Employers.objects.get(id=employer_id)
            equipment.employer = employer_instance
        except Employers.DoesNotExist:
            return Response({'error': 'Employer not found'}, status=status.HTTP_404_NOT_FOUND)

    equipment.assigned_form = data.get('assigned_form', equipment.assigned_form)
    equipment.save()

    serializer = EquipmentSerializer(equipment)
    return Response(serializer.data, status=status.HTTP_200_OK)


