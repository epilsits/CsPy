#! python3

from os import path

class RC4:
    def __init__(self, key, int rounds=1):
        self.InitKey(key, rounds)
        self.ki = 0
        self.kj = 0
        # self.gen = self.GenBytes()
        # self.gen.__next__()
    
    def InitKey(self, bytes keybytes, int rounds):
        cdef int i, j, r, kl = len(keybytes)
        cdef int key[256]
        key = [i for i in range(256)]
        j = 0
        for r in range(rounds):
            for i in range(256):
                j = (j + key[i] + keybytes[i % kl]) % 256
                key[i], key[j] = key[j], key[i]
        
        self.key = key

    ''' def GenBytes(self):
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
            l = yield out '''

    def CryptBytes(self, bytearray bytearr):
        cdef int r, i = self.ki, j = self.kj
        cdef int key[256]
        key = self.key
        cdef int bl = len(bytearr)
        for r in range(bl):
            i = (i + 1) % 256
            j = (j + key[i]) % 256
            key[i], key[j] = key[j], key[i]
            bytearr[r] ^= key[(key[i] + key[j]) % 256]
        
        self.key = key
        self.ki = i
        self.kj = j
        return bytearr

    def CryptText(self, text, encoding="iso-8859-1"):
        # same as Latin1
        arr = bytearray(text.encode(encoding))
        return self.CryptBytes(arr)

    def CryptFile(self, infile, outfile):
        if not path.isfile(infile): raise Exception("Input file does not exist.")
        with open(infile, 'rb') as src:
            with open(outfile, 'wb') as dest:
                while True:
                    data = bytearray(src.read(1048576))
                    if len(data) == 0: break
                    dest.write(self.CryptBytes(data))
                    