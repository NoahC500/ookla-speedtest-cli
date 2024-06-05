#!/bin/python3
import subprocess as os

while True:
    os.run("speedtest")
    x = input("\nTest again? Y/n: ").lower()
    if x == "n" or x == "no":
        print(f"\nExiting...\n")
        exit()
