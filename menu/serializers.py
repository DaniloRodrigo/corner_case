# snippets/serializers
from rest_framework import serializers
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('id', 'title', 'created_at', 'updated_at')


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ('id', 'title', 'restaurant', 'filepath', 'created_at', 'updated_at')


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('id', 'menu', 'employee', 'created_at', 'updated_at')


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'name', 'username', 'created_at', 'updated_at')

