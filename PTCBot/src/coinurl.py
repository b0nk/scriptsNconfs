import re, random, socks, time, socket, multiprocessing, httplib
from multiprocessing import Pool
from sys import stdout
import httplib2
from colorama import init, Fore

proxy_srcs = [line.strip() for line in open('psrc.txt', 'r')]
userAgents = [line.strip() for line in open('ua.txt', 'r')]
curl_codes = [line.strip() for line in open('coinurl/codes.txt', 'r')]

proxyList = []

def myprint(color, msg):
  t = time.strftime('%H:%M:%S', time.localtime())
  if not isinstance(msg, str):
    msg = str(msg)
  if color is 0: # Error
    print "[%s] %s" % (t, Fore.RED + msg)
  elif color is 1: # Success
    print "[%s] %s" % (t, Fore.GREEN + msg)
  elif color is 2: # INFO
    print "[%s] %s" % (t, Fore.CYAN + msg)
  elif color is 3: # Working
    print "[%s] %s" % (t, Fore.YELLOW + msg)
  elif color is 4: # Process error
    print "[%s] %s" % (t, Fore.MAGENTA + msg)
  else:
    print "[%s] %s" % (t, msg)


def reset():
  global proxyList, proxy_srcs, userAgents, curl_codes
  proxy_srcs = [line.strip() for line in open('psrc.txt', 'r')]
  userAgents = [line.strip() for line in open('ua.txt', 'r')]
  curl_codes = [line.strip() for line in open('coinurl/codes.txt', 'r')]
  proxyList = []
  myprint(2, 'Proxy list reset')
  
  
def terminate(p):
  try:
    p.terminate()
  except(WindowsError):
    myprint(4, 'Trying to terminate again...')
    time.sleep(3)
    terminate(p)


def getProxies():
  global proxy_srcs, userAgents, proxyList
  
  for i in [line.strip() for line in open('more.txt', 'r')]:
    proxyList.append(i)
    
  with open('more.txt', 'w') as f:
    f.write('')
  f.close()
  t = time.strftime('%H:%M:%S', time.localtime())
  stdout.write('\r[%s] Retrieved %s potential proxies from file' % (t, len(proxyList)))
  stdout.flush()
  stdout.write('\n')
  
  random.shuffle(proxy_srcs)
#####################################################################

  h1 = httplib2.Http(disable_ssl_certificate_validation = True, timeout = 10)
  for i in proxy_srcs:
    r, cont = h1.request(i, 'GET', headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'})
    rawList = re.findall('{.*?}', cont)
    for j in rawList:
      try:
        item = j.split(',')
        status = item[7].split(':')[1].strip('"')
        ptype = item[9].split(':')[1].strip('"')
        
        if 'OK' in status and 'Elite' or 'Anonymous' in ptype:
          ip = item[2].split(':')[1].strip('"').lstrip("0")
          port = item[4].split(':')[1].strip('"')
          port = int(port, 16)
          proxyList.append("%s:%d" % (ip, port))
      except(IndexError, ValueError):
        None
      except(socket.error) as e:
        myprint(0, e)
    t = time.strftime('%H:%M:%S', time.localtime())
    stdout.write('\r[%s] Retrieved %s potential proxies from GP' % (t, len(proxyList)))
    stdout.flush()
  stdout.write('\n')
#####################################################################
  myprint(3, "Removing duplicates...")
  proxyList = f7(proxyList)
  myprint(2, "Got a total of %s potential proxies" % (len(proxyList)))
  return proxyList

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]

def openLink(h, cc, headers):
  try:
    ticketURL = "http://schetu.net/h?cid=coinurl&a=t&r=http://cur.lv/"
    myprint(3, "Getting ticket...")
    r, cont = h.request(ticketURL, "GET", headers = headers)
    ticket = cont.split("('")[1].rstrip("');")
    link = 'http://cur.lv/redirect_curlv.php?code=%s&ticket=%s&r=http://cur.lv/'
    myprint(3, "Connecting: %s ..." % link % (cc, ticket))
    r2, cont = h.request(link % (cc, ticket), "GET", headers = headers)
    if r2:
      if r2.status is 200:
        myprint(1, "#######################SUCCESS!#######################")
        return True
  except (socket.error, httplib2.socks.HTTPError, httplib2.ServerNotFoundError, httplib2.socks.GeneralProxyError):
    return False

def visitLinks():
  global userAgents, proxyList, curl_codes
  random.shuffle(userAgents)
  random.shuffle(curl_codes)
  random.shuffle(proxyList)
  win = 0
  fail = 0
  total = len(proxyList)
  while proxyList:
    try:
      pool = Pool(1)
      myprint(2, 'Current proxy list: Success/Fail -> %s/%s | (%s/%s) | %.1f%%' % (win, fail, (win+fail)+1, total, (((win+fail+1.0)/total))*100.0))
      proxy = proxyList.pop()
      ip = proxy.split(':')[0]
      port = int(proxy.split(':')[1])
      myprint(2, 'Using proxy %s port %s' % (ip, port))
      h2 = httplib2.Http(disable_ssl_certificate_validation = True, timeout = 10,
                         proxy_info = httplib2.ProxyInfo(proxy_type = socks.PROXY_TYPE_HTTP, proxy_host = ip, proxy_port = port))
      headers = {'user-agent': random.choice(userAgents)}
      curl_code = random.choice(curl_codes)
      proc = pool.apply_async(func = openLink, args = (h2, curl_code, headers))
      res = proc.get(timeout = 11)
      if res:
        win += 1
        c = random.randint(1,4)
        while c > 0:
          curl_code = random.choice(curl_codes)
          proc = pool.apply_async(func = openLink, args = (h2, curl_code, headers))
          proc.get(timeout = 11)
          c -= 1
      else:
        fail += 1
        myprint(0, '########################FAIL!#########################')
    except(multiprocessing.pool.TimeoutError, httplib.BadStatusLine, WindowsError, IndexError):
      fail += 1
      myprint(0, '########################FAIL!#########################')
    terminate(pool)
      
init(autoreset = True)
if __name__ == "__main__":
  init(autoreset = True)
  while 1:
    getProxies()
    visitLinks()
    myprint(3, 'GETTING NEW PROXY LIST...')
    reset()
