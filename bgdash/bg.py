# -*- coding: utf-8 -*-
import logging
import json
import subprocess
import urllib2

logger = logging.getLogger(__name__)

def is_active_lane(lane):
    site_ip = lane.site.ipaddress
    lane_ip = lane.ipaddress
    return is_same_mac(site_ip, lane_ip)

def is_same_mac(site_ip, lane_ip):
    site_mac = arp(site_ip)
    lane_mac = arp(lane_ip)
    return site_mac == lane_mac and site_mac != None

def arp(ip):
  try:
    p=subprocess.Popen(["ip", "neigh"],stdout=subprocess.PIPE)
    out, err = p.communicate()
    lines = out.splitlines()
    for l in [x for x in lines if len(x) > 3]:
      record = l.split()
      if record[0] == ip:
	return record[4]
  except OSError as (errno, strerror):
    logger.error("can not resolve ip. %s: %s", (errno, strerror))
  return None



URL_TMPL = u"%(accessurl)s/static/deploy.json"

def get_deployment(lane):
  url = URL_TMPL % vars(lane)
  res = urllib2.urlopen(url).read()
  deployment = json.loads(res)
  return deployment

def get_persistent(lane):
  return {}

