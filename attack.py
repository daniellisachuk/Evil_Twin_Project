#!/use/bin/env python3
from subprocess import call
from colorama import init, Fore
init()

RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
BLUE = Fore.BLUE
RESET = Fore.RESET


print(call(["sudo", "iwconfig"]))

print(f"\n\n[>]{GREEN} Choose Monitor Interface:{RESET} ", end='')
iface = input()

print(f'[+] {BLUE}Setting {iface} to monitor {RESET}')
call(["sudo", "ifconfig", iface, "down"])
call(["sudo", "iwconfig", iface, "mode", "monitor"])
call(["sudo", "ifconfig", iface, "uo"])

call(["sudo", "airodump-ng", iface])
