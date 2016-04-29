import requests
import re
from sys import argv, stdout, getfilesystemencoding
import os

validExt = ['.jpg', '.jpeg', '.gif', '.png', '.webm']

encoding = stdout.encoding
if encoding is None:
  encoding = getfilesystemencoding()


def print_console(*args):
  try:
    print u' '.join(args).encode(encoding, 'replace')
  except UnicodeDecodeError:
    print ' '.join(args)
  except TypeError:
    print args


def goget(board, threadNo):
  baseURL = "https://i.4cdn.org/%s/%s%s"
  print "Connecting..."
  thread = requests.get('https://a.4cdn.org/%s/thread/%s.json' % (board, threadNo)).json()
  print "Processing..."
  
  total = len(thread['posts'])
  print "found %d posts" % total

  for i, post in enumerate(thread['posts']):

    timestamped = post.get('tim')
    ext = post.get('ext')

    if timestamped is None or ext not in validExt:
      continue

    link = baseURL % (board, timestamped, ext)
    
    if ext == '.jpeg':
      ext = '.jpg'
      
    original = threadNo + '-' + unicode(timestamped) + ext
    pic = requests.get(link, stream=True)
    if pic.status_code == 200:
      picsize = int(pic.headers.get('content-length'))
      filesize = 0
      try:
        filesize = int(os.path.getsize(os.path.join(u"./" + original)))
      except(WindowsError):
        pass
      if picsize != filesize:
        with open(original, "wb") as f:
          print_console(u"saving to %s" % original)
          for chunk in pic.iter_content(1024):
            f.write(chunk)
            stdout.write('\b\r(%d of %d) %s / %s bytes (%.1f%%)' % (i + 1, total, f.tell(), picsize, float(f.tell()) / float(picsize) * 100))
            stdout.flush()
          stdout.write('\n')
        f.close()
      else:
        print_console(u"%s already retrieved" % original)
        pic = None
if len(argv) < 2:
  print "missing arg"
  exit(1)

regex = re.search("http[s]?://boards.4chan.org/(\w+)/thread/(\d+)", argv[1])
if len(regex.groups()) != 2:
  print "bad url"
  exit(1)

board = regex.group(1)
threadNo = regex.group(2)

goget(board, threadNo)
