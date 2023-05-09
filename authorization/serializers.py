
from rest_framework.serializers import ModelSerializer
from authorization.models import *


class StaffSerializer(ModelSerializer):
    user = User()

    class Meta:
        model = Staff
        fields = '__all__'
