
from rest_framework.serializers import ModelSerializer
from authorization.models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StaffSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Staff
        fields = '__all__'
