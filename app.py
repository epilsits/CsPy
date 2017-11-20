#! python3

from CipherSaber import CipherSaber
from RC4 import RC4

import os
import time

# rc4 = RC4("boomstick")
# enc = rc4.CryptText("Hello World")
# rc4 = RC4("boomstick")
# dec = rc4.CryptText(enc)
# print("Encoded: {}\nDecoded: {}".format(enc, dec))

size = 100 * 1024 * 1024
rc4 = RC4("boomstick".encode("iso-8859-1"), 5)
b = bytearray(size)
start = time.perf_counter()
#print([i for i in rc4.CryptText("Hello World")])
#rc4.CryptBytes(b)
rc4.CryptFile("testfiles/file.dat.enc", "testfiles/file.dat.dec")
print("{} MB stream: {:4f}".format(size / 1024 / 1024, time.perf_counter() - start))
print("Last byte: {:#x}".format(b[-1]))

''' enc = CipherSaber().EncryptText("Hello World", "boomstick", 5)
print(type(enc))
print([i for i in enc])

dec = CipherSaber().DecryptText(enc, "boomstick", 5)
print(type(dec))
print(dec) '''

# CipherSaber().DecryptFile("testfiles/cknight.cs1", "testfiles/cknight.gif", "ThomasJefferson", 1)

# start = time.perf_counter()
# CipherSaber().EncryptFile("testfiles/file.dat", "testfiles/file.enc", "boomstick", 20)
# print("Encrypt: {:4f}".format(time.perf_counter() - start))
# start = time.perf_counter()
# CipherSaber().DecryptFile("testfiles/file.enc", "testfiles/file2.dat", "boomstick", 20)
# print("Decrypt: {:4f}".format(time.perf_counter() - start))
# os.remove("testfiles/file.enc")
# os.remove("testfiles/file2.dat")

# for i in range(10):
#     enc = CipherSaber().EncryptText("Hello World", "mykey")
#     dec = CipherSaber().DecryptText(enc, "mykey")
#     print([b for b in enc.encode("Latin1")])
#     print(dec)