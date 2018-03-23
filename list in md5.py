import os
import hashlib


def getMD5(filename):
    m = hashlib.md5()
    try:
        fd = open(filename, 'rb')
        b = fd.read();
        m.update(b)
        fd.close()
        return m.hexdigest()
    except:
        return "nothing"

file = open('test2.txt','w')
output=''
base_dir = 'd:/проекты/dmt-musical/скачанный сайт/'
for dirname, dirnames, filenames in os.walk(base_dir):
    for filename in filenames:
        fname = os.path.join(dirname, filename).replace('\\', '/')
        md5sum = getMD5(fname)
        output='{0}:{1}\n'.format(fname.replace(base_dir, ''), md5sum)
        print(output)
        file.write(output)

file.close()
