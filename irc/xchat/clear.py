__module_name__ = "Hexchat Clear command replacer"
__module_version__ = "final"
__module_description__ = "Clears window and prints channel topic/motd"
__author__ = "b0nk"

import xchat as XC

def clearWindow(word, word_eol, userdata):
  print XC.get_context()

XC.hook_command("clear", clearWindow, help="/callall and GET B&!!!")
XC.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')
