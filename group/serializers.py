from .models import Group,Membership
from rest_framework import serializers

class GroupSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True)
    class Meta:
        model = Group
        fields = ('pk','name', 'created_at', 'slug','description','members')




class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ('pk','user', 'group', 'date_joined')
