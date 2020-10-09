#!/use/bin/env python3

from subprocess import call
from time import sleep

call(["sudo", "service", "apache2", "start"])
call(["sudo", "service", "dnsmasq", "start"])
sleep(1)

with open("/etc/resolv.conf", "w") as f:
    f.write("nameserver 127.0.0.1")
sleep(1)


call(["sudo", "ifconfig", "wlan0", "up", "10.0.40.1", "netmask", "255.255.255.0"])
call(["sudo", "route", "add", "-net", "10.0.40.0", "netmask", "255.255.255.0", "gw", "10.0.40.1"])
sleep(1)

# call(["sudo", "udhcpd"])
sleep(1)

call(["sudo", "hostapd", "hostapd.conf"])
