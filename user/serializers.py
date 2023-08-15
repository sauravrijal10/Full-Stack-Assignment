from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError


from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}   

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            password =validated_data['password'],
        )
        user.password = make_password(user.password)
        try:
            user.save()
        except IntegrityError as e:
            if 'Duplicate entry' in str(e) and 'user_user.phone' in str(e):
                raise serializers.ValidationError({'phone': 'Phone number already exists.'})
            else:
                raise e
        return user 

   
