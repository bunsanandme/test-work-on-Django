from rest_framework import serializers
from .models import Organization, Event, OrganizationEvent


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", 'title', 'description', 'address', 'postcode']

class EventSerializer(serializers.ModelSerializer):
    organizations = OrganizationSerializer(many=True)
    date = serializers.DateField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'organizations', 'date']

    def create(self, validated_data):
        organizations = validated_data.pop('organizations')
        event = Event.objects.create(**validated_data)
        for organization in organizations:
            current_org, status = Organization.objects.get_or_create(
                **organization)
            OrganizationEvent.objects.create(
                organization=current_org, event=event)
        return event



