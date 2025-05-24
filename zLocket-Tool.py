# ==================================
#!/usr/bin/env python
# coding: utf-8
# Telegram: @minhkenx88
# Version: 1.0.6 (Fixed)
# Copyright by WsThanhDieu
# Description: zLocket Tool Open Source
# ==================================
import sys
import os
import struct

# --- Anti-debug checks ---
def detect_debug():
    # Method 1: sys.gettrace()
    if sys.gettrace():
        print("[!] Debugger detected (sys.gettrace)")
        sys.exit(1)

# --- Clean and run patched .pyc ---
def run_patched_pyc(pyc_path):
    with open(pyc_path, 'rb') as f:
        data = f.read()

    # Remove the fake header (12 bytes)
    clean_data = data[12:]

    # Load and execute bytecode manually (skip 16-byte pyc header)
    import marshal
    code_obj = marshal.loads(clean_data[16:])
    exec(code_obj, globals())

if __name__ == '__main__':
    detect_debug()
    run_patched_pyc('zLocket-Tool.pyc')
