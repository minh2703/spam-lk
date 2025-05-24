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

# oh my god
def detect_debug():
    # v1
    if sys.gettrace():
        print("[!] Debugger detected (sys.gettrace)")
        sys.exit(1)

    # v2
    suspicious_env = ['PYCHARM_HOSTED', 'TERM_PROGRAM', 'VSCODE_PID']
    for key in suspicious_env:
        if key in os.environ:
            print(f"[!] Suspicious environment detected: {key}")
            sys.exit(1)

# v3
def run_patched_pyc(pyc_path):
    with open(pyc_path, 'rb') as f:
        data = f.read()

    # v4
    clean_data = data[12:]

    # v5
    import marshal
    code_obj = marshal.loads(clean_data[16:])
    exec(code_obj, globals())

if __name__ == '__main__':
    detect_debug()
    run_patched_pyc('zLocket-Tool.pyc')