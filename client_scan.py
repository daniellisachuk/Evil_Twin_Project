#!/use/bin/env python3

from subprocess import call
from sys import argv

bssid = argv[1]
channel = argv[2]
iface = argv[3]

call(["airodump-ng", iface, "--bssid", bssid, "--channel", channel])
# call(["airodump-ng", iface, "--bssid", bssid, "--channel", channel, "-w", "eviltein_handshake.pcap"])
