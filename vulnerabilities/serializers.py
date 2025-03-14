from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Vulnerability, FixedVulnerability


class VulnerabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerability
        fields = '__all__'


class FixedVulnerabilitySerializer(serializers.ModelSerializer):
    vulnerability = serializers.SlugRelatedField(
        slug_field='cve_id',
        queryset=Vulnerability.objects.all()
    )
    fixed_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = FixedVulnerability
        fields = ['vulnerability', 'fixed_at', 'fixed_by']

    def validate(self, data):
        vulnerability = data.get('vulnerability')
        if FixedVulnerability.objects.filter(vulnerability=vulnerability).exists():
            raise ValidationError("Esta vulnerabilidad ya ha sido solucionada.")
        return data
