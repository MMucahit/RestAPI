from rest_framework import serializers
from titanic.models import Person

# Create your serializer here.

class PersonSerializer(serializers.ModelSerializer):
    family_size = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__' ## show all
        # exclude = ['id'] ## except id
        # read_only_fields = ['id']

    def get_family_size(self, object):
        return object.sibsp + object.parch

    def validate_age(self, age):
        if age <= 0:
            raise serializers.ValidationError('Age must be from 1 to 3')

## Standart Serializer

# class PersonSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     survived = serializers.BooleanField()    
#     pclass = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     sex = serializers.CharField(max_length=6)
#     age = serializers.FloatField()
#     sibsp = serializers.IntegerField()
#     parch = serializers.IntegerField()
#     ticket = serializers.CharField(max_length=20)
#     fare = serializers.FloatField()

#     def create(self, validated_data):
#         print(validated_data)
#         return Person.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.survived = validated_data.get('survived', instance.survived)
#         instance.pclass = validated_data.get('pclass', instance.pclass)
#         instance.name = validated_data.get('surnamevived', instance.name)
#         instance.sex = validated_data.get('sex', instance.sex)
#         instance.age = validated_data.get('age', instance.age)
#         instance.sibsp = validated_data.get('sibsp', instance.sibsp)
#         instance.parch = validated_data.get('parch', instance.parch)
#         instance.ticket = validated_data.get('ticket', instance.ticket)
#         instance.fare = validated_data.get('fare', instance.fare)
#         instance.save()
#         return instance 

#     def validate_pclass(self, value):
#         if value > 3 or value < 0:
#             raise serializers.ValidationError(f'Pclass value must be from 1 to 3 ')
#         return value    

#     def validate_age(self, value):
#         if value <= 0:
#             raise serializers.ValidationError(f'Age must be greater than zero')
#         return value                    