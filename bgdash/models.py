from django.db import models

import bg

class Site(models.Model):

    name = models.CharField(max_length=100, blank=False,)
    accessurl = models.CharField(max_length=128, blank=False,)
    hostname = models.CharField(max_length=50, blank=True,)
    ipaddress = models.CharField(max_length=50, blank=True,)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


    class Meta:
        ordering = ('created',)

class Lane(models.Model):
    site = models.ForeignKey(Site, related_name='lanes')
    name = models.CharField(max_length=100, blank=False,)
    accessurl = models.CharField(max_length=128, blank=False,)
    hostname = models.CharField(max_length=50, blank=True,)
    ipaddress = models.CharField(max_length=50, blank=True,)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def active(self):
        return bg.is_active_lane(self)

    def deployment(self):
        return bg.get_deployment(self)

    class Meta:
        ordering = ('id',)

class Build(models.Model):
    site = models.ForeignKey(Site, related_name='builds')
    name = models.CharField(max_length=100, blank=False,)
    # http://deadlock.netbeans.org/hudson/job/trunk/lastCompletedBuild/api/json
    # http://deadlock.netbeans.org/hudson/job/trunk/lastSuccessfulBuild/api/json
    accessurl = models.CharField(max_length=128, blank=False,)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
    
    def artifact(self):
        if self.id:
            return bg.get_artifact(self)
        return None
    
