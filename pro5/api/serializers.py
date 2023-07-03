from rest_framework import serializers
from api.models import Student


def name_starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with r.')
    return value

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[name_starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    #object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() == 'rohit' and ct.lower() != 'rachi':
            raise serializers.ValidationError('Rohit is from Rachi you idiot')
        return data

    #field level validation
    def validate_roll(self, value):
        if value > 199:
            raise serializers.ValidationError('Seat is Full')
        return value
