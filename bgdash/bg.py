# -*- coding: utf-8 -*-

import subprocess

def is_active_lane(lane):
    site_ip = lane.site.ipaddress
    lane_ip = lane.ipaddress
    return is_same_mac(site_ip, lane_ip)

def is_same_mac(site_ip, lane_ip):
    site_mac = arp(site_ip)
    lane_mac = arp(lane_ip)
    return site_mac == lane_mac

def arp(ip):
  p=subprocess.Popen(["ip", "neigh"],stdout=subprocess.PIPE)
  out, err = p.communicate()
  lines = out.splitlines()
  for l in [x for x in lines if len(x) > 3]:
    record = l.split()
    if record[0] == ip:
	return record[4]
  return None
