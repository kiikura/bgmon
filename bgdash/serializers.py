from django.contrib.auth.models import User, Group
from rest_framework import serializers

import models


class LaneIdsSerializer(serializers.Serializer):
    dest_lanes = serializers.ListField(
                    child=serializers.IntegerField()
                    )
    
    
    def __init__(self, site=None, **kwargs):
        super(LaneIdsSerializer, self).__init__(**kwargs)
        self.site = site
        self.dest = []
        self.src = []
        
    def validate(self, data):
        """
        Check lanid exists.
        """
        db_lanes = models.Lane.objects.filter(site=self.site)
        laneids = list(data['dest_lanes'])
        dest = []
        src = []
        for l in db_lanes:
            if l.id in laneids:
                dest.append(l)
                laneids.remove(l.id)
            else:
                src = l.id
        
        
        if  len(laneids) > 0:
            raise serializers.ValidationError("invalid dest_lanes id for current site. ids=%s" % (",".join(map(str, laneids))))
        
        self.dest = dest
        self.src = src
        return data

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

class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Build
        fields = ("id",
                "name",
                "accessurl",
                "artifact",
                "created",
                "modified",)

class SiteSerializer(serializers.ModelSerializer):
    lanes = LaneSerializer(many=True, read_only=True)
    builds = BuildSerializer(many=True, read_only=True)
    
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
