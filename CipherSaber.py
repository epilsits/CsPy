#! python3

from os import path
from os import urandom
from RC4 import RC4

class CipherSaber:
    def EncryptFile(self, infile, outfile, key, rounds=20, encoding="iso-8859-1"):
        if not path.isfile(infile): raise Exception("Input file does not exist.")
        with open(infile, 'rb') as src:
            with open(outfile, 'wb') as dest:
                iv = urandom(10)
                dest.write(iv)
                keybytes = key[:246].encode(encoding) + iv
                rc4 = RC4(keybytes, rounds)
                while True:
                    data = bytearray(src.read(1048576))
                    if len(data) == 0: break
                    dest.write(rc4.CryptBytes(data))

    def DecryptFile(self, infile, outfile, key, rounds=20, encoding="iso-8859-1"):
        if not path.isfile(infile): raise Exception("Input file does not exist.")
        with open(infile, 'rb') as src:
            with open(outfile, 'wb') as dest:
                keybytes = key[:246].encode(encoding) + src.read(10)
                rc4 = RC4(keybytes, rounds)
                while True:
                    data = bytearray(src.read(1048576))
                    if len(data) == 0: break
                    dest.write(rc4.CryptBytes(data))

    def EncryptText(self, text, key, rounds=20, encoding="iso-8859-1"):
        iv = urandom(10)
        keybytes = key[:246].encode(encoding) + iv
        rc4 = RC4(keybytes, rounds)
        return iv + rc4.CryptText(text, encoding)

    def DecryptText(self, data, key, rounds=20, encoding="iso-8859-1"):
        keybytes = key[:246].encode(encoding) + data[:10]
        rc4 = RC4(keybytes, rounds)
        return rc4.CryptBytes(bytearray(data[10:])).decode(encoding)
        