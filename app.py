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

size = 10 * 1024 * 1024
start = time.perf_counter()
rc4 = RC4("boomstick", 1)
b = rc4.gen.send(size)
print("{} MB stream: {:4f}".format(size / 1024 / 1024, time.perf_counter() - start))
print("Last byte: {:#x}".format(b[-1]))

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