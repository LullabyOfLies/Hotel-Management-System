from rest_framework import serializers
from .models import Admins

class AdminSerializers(serializers.ModelSerializer):

    class Meta:
        model = Admins
        fields = (
            'pk',
            'username',
            'email',
            'last_name',
            'first_name',
            'middle_name',
        )