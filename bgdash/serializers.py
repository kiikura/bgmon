from django.contrib.auth.models import User, Group
from rest_framework import serializers

import models



class LaneSerializer(serializers.ModelSerializer):
    active = serializers.ReadOnlyField()

    class Meta:
        model = models.Lane
        fields = ("id",
                "name",
            "accessurl",
            "hostname",
            "ipaddress",
            "active",
            "deployment",
            "created",
            "modified",)

class SiteSerializer(serializers.ModelSerializer):
    lanes = LaneSerializer(many=True, read_only=True)
    class Meta:
        model = models.Site
        fields = ('id', 'name', 'hostname', 'accessurl', 'lanes', 'builds', 'created', 'modified')

class ListSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Site


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
