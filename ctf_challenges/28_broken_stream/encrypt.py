#!/usr/bin/env python3
"""
Broken AES encryption with static IV vulnerability
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

# STATIC IV - THIS IS THE VULNERABILITY!
IV = b'1234567890123456'  # Static IV - same for all encryptions
KEY = os.urandom(16)

def encrypt(plaintext):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    padded = pad(plaintext.encode(), AES.block_size)
    return cipher.encrypt(padded)

if __name__ == "__main__":
    flag = "school21{rb6a7czcaf}"
    encrypted = encrypt(flag)
    with open("flag.enc", "wb") as f:
        f.write(encrypted)
    print("Flag encrypted to flag.enc")
    print("Hint: Static IV vulnerability allows decryption!")

