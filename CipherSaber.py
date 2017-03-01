#! python3

from os import path
from os import urandom
from RC4 import RC4

class CipherSaber:
    def EncryptFile(self, infile, outfile, key, rounds=20):
        if not path.isfile(infile): raise Exception("Input file does not exist.")
        with open(infile, 'rb') as src:
            with open(outfile, 'wb') as dest:
                iv = urandom(10)
                dest.write(iv)
                keytext = key[:246] + "".join([chr(b) for b in iv])
                rc4 = RC4(keytext, rounds)
                while True:
                    data = bytearray(src.read(1048576))
                    if len(data) == 0: break
                    dest.write(rc4.Rc4CryptBytes(data))

    def DecryptFile(self, infile, outfile, key, rounds=20):
        if not path.isfile(infile): raise Exception("Input file does not exist.")
        with open(infile, 'rb') as src:
            with open(outfile, 'wb') as dest:
                keytext = key[:246] + "".join([chr(b) for b in src.read(10)])
                rc4 = RC4(keytext, rounds)
                while True:
                    data = bytearray(src.read(1048576))
                    if len(data) == 0: break
                    dest.write(rc4.Rc4CryptBytes(data))

import time

rc4 = RC4("boomstick")
enc = rc4.Rc4CryptText("Hello World")
rc4 = RC4("boomstick")
dec = rc4.Rc4CryptText(enc)
print("Encoded: {}\nDecoded: {}".format(enc, dec))

# rc4 = RC4("boomstick", 1)
# start = time.perf_counter()
# size = 5 * 1024 * 1024
# for i in range(size):
#     b = rc4.gen.__next__()
# print("{} MB stream: {:4f}".format(size / 1024 / 1024, time.perf_counter() - start))
# print("Last byte: {:#x}".format(b))

# CipherSaber().EncryptFile("file.dat", "file.enc", "boomstick", 20)
# print("Encrypt: {:4f}".format(time.perf_counter() - start))
# start = time.perf_counter()
# CipherSaber().DecryptFile("file.enc", "file2.dat", "boomstick", 20)
# print("Decrypt: {:4f}".format(time.perf_counter() - start))