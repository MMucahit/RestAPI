from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from titanic.models import Person
from titanic.api.serializers import PersonSerializer

# Create your views here.

@api_view(['GET'])
def person_list_sex(request,sex):
    try:
        person_instance = Person.objects.filter(sex=sex)
    except Person.DoesNotExist:
        return Response({'errors':{'code':404,'message':'Dont exist!'}}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(person_instance, many=True)
        return Response(serializer.data)


@api_view(['GET','POST'])
def person_list_create_api_view(request):
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    

        return Response(status=status.HTTP_400_BAD_REQUEST)    


@api_view(['GET','PUT','DELETE'])
def person_detail_api_view(request, pk):
    try:
        person_instance = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response({'errors':{'code':404,'message':'Dont exist!'}}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(person_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(person_instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    

        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)