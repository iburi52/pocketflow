from rest_framework import serializers
from .models import Archive


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = "__all__"

        extra_kwargs = {
            'created_by':  { 'read_only': True }
        }