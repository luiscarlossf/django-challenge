from django.contrib.auth.models import User
from .models import RegularPlan
from rest_framework import serializers

class RegularPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegularPlan
        fields = [
            'id',
            'name',
            'tar_included',
            'subscription',
            'cycle',
            'type',
            'offer_iva',
            'off_peak_price',
            'peak_price',
            'unit',
            'valid',
            'publish',
            'vat',
            'owner',
        ]