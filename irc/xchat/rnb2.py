__module_name__ = "Hexchat Eye Cancer Plugin"
__module_version__ = "0.1"
__module_description__ = "Eye Cancer"
__author__ = "b0nk"

import xchat as XC
from random import randint


def make_a_cancer(word, word_eol, userdata):

  COLOR = '\003'
  original = XC.strip(word_eol[1])
  original = original.upper()
  cancered = ''
  i = 0
  while i < 20:

    ran1 = randint(3, 15)
    ran2 = randint(3, 15)

    if ran1 == ran2:
      ran2 = randint(3, 15)

    cancered += "%s%d,%d" % (COLOR, ran1, ran2) + original
    i += 1

  XC.command('say %s' % (cancered))

XC.hook_command("rnb2", make_a_cancer, help="/rnb2 <text>")
XC.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')
