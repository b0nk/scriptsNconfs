__module_name__ = "Hexchat True Rainbow Plugin"
__module_version__ = "0.1"
__module_description__ = "True Rainbow"
__author__ = "b0nk"

import xchat as XC


def make_a_rainbow(word, word_eol, userdata):

  original = XC.strip(word_eol[1])
  sequence = ['04', '07', '08', '03', '12', '02', '06']
  length = len(original)
  counter = len(sequence)
  colored = ''
  COLOR = '\003'
  i = 0
  num = 0

  while(i <= length - 1):

    if(i >= counter):
      num = i - counter

      while(num >= counter):
        num -= counter

    else:
      num = i

    tmp = COLOR + sequence[num] + original[i]
    colored = colored + tmp
    i += 1

  XC.command('say %s' % (colored + COLOR))

XC.hook_command("rnb", make_a_rainbow, help="/rnb <text>")
XC.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')
