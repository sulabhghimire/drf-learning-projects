from rest_framework import serializers
from api.models import Student


class StudentSerializers(serializers.ModelSerializer):

    def name_starts_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with r.')
        return value

    # name = serializers.CharField(read_only = True)
    name = serializers.CharField(validators=[name_starts_with_r])

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['id', 'name', 'roll', 'city']
        # read_only_fields = ['name', 'roll']
        # extra_kwargs = {'name': {'read_only':True}}

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