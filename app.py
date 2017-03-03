#! python3

from CipherSaber import CipherSaber
from RC4 import RC4

import time

# rc4 = RC4("boomstick")
# enc = rc4.Rc4CryptText("Hello World")
# rc4 = RC4("boomstick")
# dec = rc4.Rc4CryptText(enc)
# print("Encoded: {}\nDecoded: {}".format(enc, dec))

# rc4 = RC4("boomstick", 1)
# start = time.perf_counter()
# size = 5 * 1024 * 1024
# for i in range(size):
#     b = rc4.gen.__next__()
# print("{} MB stream: {:4f}".format(size / 1024 / 1024, time.perf_counter() - start))
# print("Last byte: {:#x}".format(b))

CipherSaber().DecryptFile("testfiles\cknight.cs1", "testfiles\cknight.gif", "ThomasJefferson", 1)

# CipherSaber().EncryptFile("testfiles\file.dat", "file.enc", "boomstick", 20)
# print("Encrypt: {:4f}".format(time.perf_counter() - start))
# start = time.perf_counter()
# CipherSaber().DecryptFile("testfiles\file.enc", "file2.dat", "boomstick", 20)
# print("Decrypt: {:4f}".format(time.perf_counter() - start))

# for i in range(10):
#     enc = CipherSaber().EncryptText("Hello World", "mykey")
#     dec = CipherSaber().DecryptText(enc, "mykey")
#     print([b for b in enc.encode("Latin1")])
#     print(dec)