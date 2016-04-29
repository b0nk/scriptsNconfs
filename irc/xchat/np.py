__module_name__ = "Hexchat AMIP Announcer"
__module_version__ = "0.1"
__module_description__ = "Announces the currently played song using AMIP"
__author__ = "Johan Ljungberg"

AMIP_FILE = 'd:/amip.txt'  # Update this path to reflect your configuration

import xchat as XC

def nowplaying_cb(word, word_eol, userdata):
  try:
    with open(AMIP_FILE, 'r') as f:
      title = f.read().split(' || ')[0]
      XC.command('me listens to: %s' % title)
  except IOError:
    print 'ERROR: Could not read %s, have you configured the plugin properly?' % AMIP_FILE

XC.hook_command("np", nowplaying_cb, help="/np Announces the currently played song using AMIP")
XC.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')
