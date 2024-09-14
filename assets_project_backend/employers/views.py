from django.http import HttpResponse, JsonResponse

from .models import Employers
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import EmployerSerializer
@csrf_exempt
@api_view(['POST'])
def addEmployers(request):
    if request.method == 'POST':
        serializer = EmployerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employer added successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getEmployers(request):
    employers = Employers.objects.all()
    serializer = EmployerSerializer(employers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getEmployersData(request):
    employers = list(Employers.objects.values('id', 'name', 'surname'))  # Customize this query as needed
    return JsonResponse(employers, safe=False)

@api_view(['GET'])
def getEmployerById(request, id):
    print(f"Received request for id: {id}")
    try:
        employer = Employers.objects.get(id=id)
    except Employers.DoesNotExist:
        return Response({'error': 'Equipment not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = EmployerSerializer(employer)
    return Response(serializer.data)

