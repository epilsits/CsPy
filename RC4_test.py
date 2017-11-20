from RC4 import RC4
from filecmp import cmp
import os

class TestRC4(object):
    def test_rc4text(self):
        p = "boomstick"
        r = 5
        t = "Hello World"
        encoding = "Latin1"
        rc4 = RC4(p.encode(encoding), r)
        e = rc4.CryptText(t)
        rc4 = RC4(p.encode(encoding), r)
        d = rc4.CryptText(e.decode(encoding)).decode(encoding)

        assert d == t

    def test_rc4file(self):
        p = "boomstick"
        r = 5
        encoding = "Latin1"
        rc4 = RC4(p.encode(encoding), r)
        rc4.CryptFile("testfiles\\file.dat", "testfiles\\file.dat.enc")
        assert not cmp("testfiles\\file.dat", "testfiles\\file.dat.enc", False)

        rc4 = RC4(p.encode(encoding), r)
        rc4.CryptFile("testfiles\\file.dat.enc", "testfiles\\file.dat.dec")
        assert cmp("testfiles\\file.dat", "testfiles\\file.dat.dec", False)

        os.remove("testfiles\\file.dat.enc")
        os.remove("testfiles\\file.dat.dec")

    def bench_rc4bytes(self, rc4, buff):
        rc4.CryptBytes(buff)

    def test_benchbytes(self, benchmark):
        encoding = "Latin1"
        size = 10 * 1024 * 1024
        b = bytearray(size)
        rc4 = RC4("boomstick".encode(encoding), 5)
        benchmark(self.bench_rc4bytes, rc4, b)