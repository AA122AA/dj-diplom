from rest_framework import fields, serializers

from shop.models import Project, Measurement

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 'name', 
            'latitude', 'longitude', 
            'created_at', 'updated_at'
        ]

    
class MeasurmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = [
            'id', 'value', 'project', 
            'created_at', 'updated_at',
            'image'
        ]   