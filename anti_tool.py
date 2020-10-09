from scapy.all import sniff
from colorama import init, Fore

init()

count = 0

def sniff_deauth(pkt):
    global count
#    print "got pkt"
    if pkt.haslayer(Dot11FCS):
        if pkt.type == 0 and pkt.subtype == 0xc:
	    count = count + 1
    if count >= 20:
        print(f"{Fore.RED}WARNING! -\nNumber of deauth packets in the system has exeeded the threshhold\n Your AP might be under deauth-attack{Fore.RESET}")

sniff(iface="wlan0", prn = sniff_deauth)
