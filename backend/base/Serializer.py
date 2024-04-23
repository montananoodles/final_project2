from rest_framework import serializers
from .models import UserProfile, CustomerProfile, SellerProfile, Service, PicsPosts, Appointment, NextAppointment

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'

class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class PicsPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PicsPosts
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class NextAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextAppointment
        fields = '__all__'
