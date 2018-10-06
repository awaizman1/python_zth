
# Given an encrypted binary file (encrypted.bin) and a cipher text file (cipher.txt), decrypted the file and
# print it's content.
# The cipher.txt is of format:
# ascii_code --> byte_code

import random
import string
import sys


def load_cipher():
    """
    Loads 'cipher.txt'
    :return: bytearray where output[byte_code] = ascii_code
    """

    cipher = bytearray(256)
    with open("cipher.txt", mode='r') as f:
        lines = f.read().splitlines()
        for line in lines:
            char, code = line.split(" --> ")
            cipher[int(code)] = int(char)

    return cipher


def decrypt(encrypted, cipher):
    """
    Decyptes encrypted using cipher
    :param encrypted: encrypted text as bytes
    :param cipher: bytes where cipher[byte_code] = ascii_code
    :return: the decrypted str
    """
    res = bytearray(len(encrypted))
    for index in range(len(encrypted)):
        res[index] = cipher[encrypted[index]]

    return res.decode()


def decrypt_file(encrypted_file, cipher_file):
    cipher = load_cipher()

    with open(encrypted_file, mode='rb') as enc:
        encrypted = enc.read()

    return decrypt(encrypted, cipher)


def create_cipher():
    for c in string.printable:
        codes = list(range(256))
        random.shuffle(codes)

        with open("cipher.txt", mode='w') as f:
            for char, code in zip(string.printable, codes):
                f.write(f"{ord(char)} --> {code}\n")


def create_encrypted():
    cipher = load_cipher()

    text = """Very good!
It seems you are now mastering python bytes.
Did you solve this without keeping concatenating into an immutable str?
If not try again..."""

    with open('encrypted.bin', mode='wb') as f:
        for c in text:
            f.write(cipher.index(ord(c)).to_bytes(1, sys.byteorder))


print(decrypt_file("encrypted.bin", "cipher.txt"))
