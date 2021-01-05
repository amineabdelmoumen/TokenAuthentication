from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['email','username','password','password1']
        extra_kwargs= {
            'password':{'write_only':True}
            
        }
    def save(self):
        account=User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password1=self.validated_data['password1']
        password=self.validated_data['password']
        if password != password1:
            raise serializers.ValidationError({'password1':'the password must match'})
        else:
            account.set_password(password)
            account.save()
            return account
