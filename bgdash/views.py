from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from bgdash.serializers import (
    SiteSerializer,
    LaneSerializer,
    UserSerializer,
    GroupSerializer,
    )
from bgdash import models

import subprocess



class SiteViewSet(viewsets.ModelViewSet):
    serializer_class = SiteSerializer
    queryset = models.Site.objects.all()



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
