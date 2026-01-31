#!/usr/bin/python3
import subprocess, re, sys

# Hacknet Minimal Theme
C, G, R, E, B = '\033[96m', '\033[92m', '\033[91m', '\033[0m', '\033[1m'

def get_info(ip):
    try:
        ping = subprocess.check_output(f"ping -c 1 -W 2 {ip}", shell=True).decode()
        ttl = int(re.search(r"ttl=(\d+)", ping).group(1))
        os = f"{G}Linux" if ttl <= 64 else f"{C}Windows" if ttl <= 128 else f"{Y}Network Device (Cisco/Solaris/BSDs)"
        return ttl, os
    except:
        return None, f"{R}Unreachable"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"\n{R}[!] Usage: python3 {sys.argv[0]} <ip>{E}"); sys.exit(1)

    print(f"\n{C}{B}  WHICH-HOST | Hacknet{E}\n  {'-'*21}")
    ttl, os = get_info(sys.argv[1])
    print(f"  {B}Target:{E} {sys.argv[1]}\n  {B}TTL:{E}    {ttl or 'N/A'}\n  {B}OS:{E}     {os}{E}\n")
