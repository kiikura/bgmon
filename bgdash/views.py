# -*- coding: utf-8 -*-

import subprocess

from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from bgdash.serializers import (
    ListSiteSerializer,
    SiteSerializer,
    LaneSerializer,
    UserSerializer,
    GroupSerializer,
    LaneIdsSerializer
    )
from bgdash import models





class SiteViewSet(viewsets.ModelViewSet):
    serializer_class = SiteSerializer
    queryset = models.Site.objects.all()

    def get_serializer_class(self):
        if "pk" in self.kwargs:
            return self.serializer_class
        else:
            return ListSiteSerializer

    @detail_route(methods=['post'])
    def switch(self, request, pk=None):
        site = self.get_object()
        serializer = LaneIdsSerializer(data=dict(request.data),site=site)
        if serializer.is_valid():
            print serializer.dest
            return Response({'status': serializer.data})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

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
