import py_compile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from titanic.models import Person
from titanic.api.serializers import PersonSerializer

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


    # def data(self):
    #     import json
    #     import mysql.connector
    #     mydb = mysql.connector.connect(host="127.0.0.1",user="root",password="30918",database="person")

    #     mycursor = mydb.cursor()

    #     mycursor.execute("SELECT * FROM titanic_person")

    #     content = {}
    #     payload = []
    #     for i in mycursor.fetchall():
    #         content = {Person.columns_list[j]: i[j] for j in range(len(Person.columns_list))}
    #         payload.append(content)
    #         content = {}

    #     return json.dumps(payload, indent=2, sort_keys=True)  


# Create your views here.

class PersonListSexAPIView(APIView):
    def get_object(self, sex):
        person_instance = get_object_or_404(Person, pk=sex)
        return person_instance

    def get(self, request, sex):
        person_instance = Person.objects.filter(sex=sex)
        serializer = PersonSerializer(person_instance, many=True)
        return Response(serializer.data)


class PersonListCreateAPIView(APIView):

    def get(self, request):
        person_instance = Person.objects.all()
        serializer = PersonSerializer(person_instance, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    

        return Response(status=status.HTTP_400_BAD_REQUEST)    


class PersonDetailAPIView(APIView):
    def get_object(self, pk):
        person_instance = get_object_or_404(Person, pk=pk)
        return person_instance

    def get(self, request, pk):    
        person_instance = self.get_object(pk=pk)
        serializer = PersonSerializer(person_instance)
        return Response(serializer.data)

    def put(self, request, pk):
        person_instance = self.get_object(pk=pk)
        serializer = PersonSerializer(person_instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        person_instance = self.get_object(pk=pk)
        person_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



## Function Based!

# @api_view(['GET'])
# def person_list_sex(request,sex):
#     try:
#         person_instance = Person.objects.filter(sex=sex)
#     except Person.DoesNotExist:
#         return Response({'errors':{'code':404,'message':'Dont exist!'}}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PersonSerializer(person_instance, many=True)
#         return Response(serializer.data)


# @api_view(['GET','POST'])
# def person_list_create_api_view(request):
#     if request.method == 'GET':
#         person = Person.objects.all()
#         serializer = PersonSerializer(person, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)    

#         return Response(status=status.HTTP_400_BAD_REQUEST)    


# @api_view(['GET','PUT','DELETE'])
# def person_detail_api_view(request, pk):
#     try:
#         person_instance = Person.objects.get(pk=pk)
#     except Person.DoesNotExist:
#         return Response({'errors':{'code':404,'message':'Dont exist!'}}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PersonSerializer(person_instance)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PersonSerializer(person_instance,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)    

#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         person_instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)