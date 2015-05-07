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
        p = subprocess.Popen(["ip", "neigh"], stdout=subprocess.PIPE)
        out, err = p.communicate()
        lines = out.splitlines()
        for l in [x for x in lines if len(x) > 3]:
            record = l.split()
            if record[0] == ip:
                return record[4]
    except OSError as e:
        logger.error("can not resolve IP address. %s : %s", e.errno, e.strerror)
    return None



URL_TMPL = u"%(accessurl)s/static/deploy.json"

def get_deployment(lane):
    try:
        url = URL_TMPL % vars(lane)
        res = urllib2.urlopen(url, None, 5).read()
        deployment = json.loads(res)
        return deployment
    except:
        logger.error("can not get deployment. url=%s", url)
        return "#ERROR"

def get_persistent(lane):
    return {}


def get_artifact(build):
    try:
        url = build.accessurl
        res = urllib2.urlopen(url, None, 5).read()
        art = json.loads(res)
        return art
    except:
        logger.error("can not get build artifacts. url=%s", url)
        return "#ERROR"
    


