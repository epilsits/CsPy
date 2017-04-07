#! python3

from os import path

class RC4:
    def __init__(self, key, int rounds=1, encoding="iso-8859-1"):
        if isinstance(key, str):
            key = key.encode(encoding)
        self.InitKey(key, rounds)
        self.gen = self.GenBytes()
        self.gen.__next__()
    
    def InitKey(self, bytes keybytes, int rounds):
        cdef int kl = len(keybytes)
        cdef int i, r
        self.key = [i for i in range(256)]
        cdef int j = 0
        for r in range(rounds):
            for i in range(256):
                j = (j + self.key[i] + keybytes[i % kl]) % 256
                self.key[i], self.key[j] = self.key[j], self.key[i]

    def GenBytes(self):
        cdef int i = 0, j = 0, k, l
        cdef int key[256]
        for i in range(256):
            key[i] = self.key[i]
        i = 0
        l = yield
        while True:
            out = []
            for k in range(l):
                i = (i + 1) % 256
                j = (j + key[i]) % 256
                key[i], key[j] = key[j], key[i]
                out.append(key[(key[i] + key[j]) % 256])
            l = yield out

    def CryptBytes(self, bytearray bytearr):
        cryptbytes = self.gen.send(len(bytearr))
        cdef int i
        for i in range(len(bytearr)):
            bytearr[i] = bytearr[i] ^ cryptbytes[i]
        return bytearr

    def CryptText(self, text, encoding="iso-8859-1"):
        # same as Latin1
        arr = bytearray(text.encode(encoding))
        return self.CryptBytes(arr).decode(encoding)

    def CryptFile(self, infile, outfile):
        if not path.isfile(infile): raise Exception("Input file does not exist.")
        with open(infile, 'rb') as src:
            with open(outfile, 'wb') as dest:
                while True:
                    data = bytearray(src.read(1048576))
                    if len(data) == 0: break
                    dest.write(self.CryptBytes(data))
                    