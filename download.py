import requests
import os
from sys import stdout


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0',
           'referer': ''}


def download(link):
  file = requests.get(link, stream=True, headers=headers)
  filename = link.split('/')[-1]
  if file.status_code == 200:
    size = int(file.headers.get('content-length'))
    filesize = 0
    try:
      filesize = int(os.path.getsize(os.path.join('./' + filename)))
    except(WindowsError):
      pass
    if size != filesize:
      with open(os.path.join('./' + filename), 'wb') as f:
        print 'saving to %s' % filename
        for chunk in file.iter_content(1024):
          f.write(chunk)
          stdout.write('\b\r %s / %s bytes (%.1f%%)' % (f.tell(), size, float(f.tell()) / float(size) * 100))
          stdout.flush()
        stdout.write('\n')
      f.close()
    else:
      print '%s already retrieved' % filename
