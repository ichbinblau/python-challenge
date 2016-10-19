# answer: http://www.pythonchallenge.com/pc/hex/copper.html

from zipfile import ZipFile
import zlib
import bz2

PWD='redavni'

zipfile = ZipFile("21.zip")
zipfile.extractall(pwd=PWD)

log = []

with open("package.pack", 'rb') as f:
    data = f.read()

    while True:
        # zip format
        if data.startswith(b'x\x9c'):
            data = zlib.decompress(data)
            log.append(' ')
        # bz2 format
        elif data.startswith(b'BZh'):
            data = bz2.decompress(data)
            log.append('#')
        # reverse zip format
        elif data.endswith(b'\x9cx'):
            data = data[::-1]
            log += '\n'
        else:
            break

print "".join(log) 
