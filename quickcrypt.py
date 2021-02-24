#!/usr/bin/env python

import random
import sys

from getpass import getpass


PREFIXES = {
    1: [1, 4, 7, "a", "d"],
    2: [2, 5, 8, "b", "e"],
    3: [3, 6, 9, "c", "f"],
}


def hexify(num):
    hx = str(hex(num))[2:]
    prefix = random.choice(PREFIXES[len(hx)])
    return f"{prefix}{hx}"


def encrypt(message, password):
    encrypted = ""
    for i in range(len(message)):
        pi = i % len(password)
        encrypted += hexify(ord(message[i]) + ord(password[pi]))
    return encrypted


def decrypt(message, password):
    decrypted = ""
    i = 0
    pi = 0
    while i < len(message):
        hl = ((int(message[i], 16) - 1) % 3) + 1
        i += 1 + hl
        c = chr(int(message[i-hl:i], 16) - ord(password[pi]))
        decrypted += c
        pi = (pi + 1) % len(password)
    return decrypted


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
    else:
        print("Error: Missing command.")
        exit(1)

    if command in ("encrypt", "decrypt"):
        if len(sys.argv) > 2:
            msg = sys.argv[2]
        else:
            msg = input("Message: ")
        password = getpass("Password: ")
        if command == "encrypt":
            print(encrypt(msg, password))
        elif command == "decrypt":
            print(decrypt(msg, password))
    else:
        print("Error: Invalid command.")


if __name__ == "__main__":
    main()

