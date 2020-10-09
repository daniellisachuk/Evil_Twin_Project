from scapy.all import sniff




count = 0

def sniff_deauth(pkt):
    global count
#    print "got pkt"
    if pkt.haslayer(Dot11FCS):
        if pkt.type == 0 and pkt.subtype == 0xc:
	    count = count + 1
    if count >= 20:
        print("warning you'r AP is under deauth-attack")

sniff(iface="wlan0", prn = sniff_deauth)
