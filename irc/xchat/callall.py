__module_name__ = "Hexchat Call ALL"
__module_version__ = "final"
__module_description__ = "GET B&"
__author__ = "b0nk"

import xchat as XC

def ca(word, word_eol, userdata):
  try:
    XC.command('say %s' % (' '.join(i.nick for i in XC.get_list('users'))))
  except Exception as e:
    print e

XC.hook_command("callall", ca, help="/callall and GET B&!!!")
XC.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')
