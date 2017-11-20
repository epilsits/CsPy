#! python3

from os import path

class RC4:
    def __init__(self, key, rounds=1):
        self.InitKey(key, rounds)
        self.ki = 0
        self.kj = 0
        #self.gen = self.GenBytes()
    
    def InitKey(self, keybytes, rounds):
        kl = len(keybytes)
        self.key = [i for i in range(256)]
        j = 0
        for r in range(rounds):
            for i in range(256):
                j = (j + self.key[i] + keybytes[i % kl]) % 256
                self.key[i], self.key[j] = self.key[j], self.key[i]

    ''' def GenBytes(self):
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + self.key[i]) % 256
            self.key[i], self.key[j] = self.key[j], self.key[i]
            yield self.key[(self.key[i] + self.key[j]) % 256] '''

    def CryptBytes(self, bytearr):
        i, j = self.ki, self.kj
        key = self.key
        for r in range(len(bytearr)):
            i = (i + 1) % 256
            j = (j + key[i]) % 256
            key[i], key[j] = key[j], key[i]
            bytearr[r] ^= key[(key[i] + key[j]) % 256]
        
        self.ki, self.kj = i, j
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
                    