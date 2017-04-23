import requests
import os
import re
import json
import urllib
from sys import argv, stdout, getfilesystemencoding


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

def getValidBoards():
  boards = []

  l = json.load(urllib.urlopen('https://a.4cdn.org/boards.json'))

  for i in l['boards']:
    boards.append(str(i['board']))

  return boards


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

board = None
threadNo = None

if len(argv) == 2:
  regex = re.search("http[s]?://boards.4chan.org/(\w+)/thread/(\d+)", argv[1])
  if regex and len(regex.groups()) == 2:
    board = regex.group(1)
    threadNo = regex.group(2)
  else:
    print "bad url"
    exit(1)

elif len(argv) == 3:
  board = argv[1]
  threadNo = argv[2]

  # check if it's a board and a number
  print "Verifying args..."
  if not threadNo.isdigit():
    print "%s is not a thread number" % threadNo
    exit(1)

  valid_boards = getValidBoards()
  if board not in valid_boards:
    print "/%s/ is not a real board" % board
    exit(1)



else:
  print "bad args! Usage: $ getthread.py [link to thread] | [board] [threadNumber]"
  exit(1)

goget(board, threadNo)
