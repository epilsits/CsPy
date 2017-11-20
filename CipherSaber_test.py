from CipherSaber import CipherSaber
import os
from filecmp import cmp

class TestCipherSaber(object):
    def test_cstext(self):
        p = "boomstick"
        r = 5
        t = "Hello World"
        enc = CipherSaber().EncryptText(t, p, r)
        dec = CipherSaber().DecryptText(enc, p, r)
        assert dec == t

    def test_csfile(self):
        p = "boomstick"
        r = 5
        CipherSaber().EncryptFile("testfiles\\file.dat", "testfiles\\file.dat.enc", p, r)
        assert not cmp("testfiles\\file.dat", "testfiles\\file.dat.enc", False)

        CipherSaber().DecryptFile("testfiles\\file.dat.enc", "testfiles\\file.dat.dec", p, r)
        assert cmp("testfiles\\file.dat", "testfiles\\file.dat.dec", False)

        os.remove("testfiles\\file.dat.enc")
        os.remove("testfiles\\file.dat.dec")

    def bench_file(self, f):
        p = "boomstick"
        r = 5
        o = f + ".enc"
        CipherSaber().EncryptFile(f, o, p, r)
        return o

    def test_benchfile(self, benchmark):
        f = "testfiles\\tmp.dat"
        size = 100 * 1024 * 1024
        with open(f, "wb") as fp:
            fp.write(os.urandom(size))

        o = benchmark(self.bench_file, f)
        os.remove(f)
        os.remove(o)

    def bench_text(self, buff):
        p = "boomstick"
        r = 5
        CipherSaber().DecryptText(buff, p, r)

    def test_benchtext(self, benchmark):
        size = 100 * 1024 * 1024
        b = os.urandom(size)
        benchmark(self.bench_text, b)