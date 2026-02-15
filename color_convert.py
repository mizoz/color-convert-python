#!/usr/bin/env python3
"""Convert between color formats (HEX, RGB, HSL)."""
import sys, re

def hex_to_rgb(h): h = h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in(0,2,4))
def rgb_to_hex(r,g,b): return f"#{r:02x}{g:02x}{b:02x}"

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: color_convert.py <#hex|rgb(r,g,b)>"); sys.exit(1)
    v = sys.argv[1]
    if v.startswith('#'): print(f"RGB: {hex_to_rgb(v)}")
    elif v.startswith('rgb'): m=re.findall(r'\d+',v); print(f"HEX: {rgb_to_hex(*map(int,m))}")
