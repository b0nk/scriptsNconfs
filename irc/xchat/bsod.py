__module_name__ = "Hexchat BSOD"
__module_version__ = "final"
__module_description__ = "BSODs the target"
__author__ = "Anonymous"

import xchat as XC
from hclib import COLOR, UNDERLINE, BOLD

def bsod(word, word_eol, userdata):
  try:
    XC.command("say %s%s                                                " % (UNDERLINE, (COLOR + '12,12')))
    XC.command("say %s%s                                                " % (UNDERLINE, (COLOR + '12,12')))
    XC.command("say %s%s                                                " % (UNDERLINE, (COLOR + '12,12')))
    XC.command("say %s%s                    %s%s%sWindows%s%s%s                     " % (UNDERLINE, (COLOR + '12,12'), BOLD, (COLOR + '12,15'), UNDERLINE, UNDERLINE, BOLD, (COLOR + '12,12')))
    XC.command("say %s%s                                                " % (UNDERLINE, (COLOR + '12,12')))
    XC.command("say %s%s   %s%s%sA fatal exception has occurred in internets%s%s%s  " % (UNDERLINE, (COLOR + '12,12'), UNDERLINE, BOLD, (COLOR + '15,12'), UNDERLINE, BOLD, (COLOR + '12,12')))
    XC.command("say %s%s   %s%s%sThe current application will be terminated.%s%s%s  " % (UNDERLINE, (COLOR + '12,12'), UNDERLINE, BOLD, (COLOR + '15,12'), UNDERLINE, BOLD, (COLOR + '12,12')))
    XC.command("say %s%s                                                " % (UNDERLINE, (COLOR + '12,12')))
    XC.command("say %s%s   %s%s%s* Press any key to terminate%s%s%s                 " % (UNDERLINE, (COLOR + '12,12'), UNDERLINE, BOLD, (COLOR + '15,12'), UNDERLINE, BOLD, (COLOR + '12,12')))
    XC.command("say %s%s   %s%s%s* Press ALT+Z and assume fetal position. You%s%s%s " % (UNDERLINE, (COLOR + '12,12'), UNDERLINE, BOLD, (COLOR + '15,12'), UNDERLINE, BOLD, (COLOR + '12,12')))
    XC.command("say %s%s     %s%s%swill lose any unsaved information.%s%s%s         " % (UNDERLINE, (COLOR + '12,12'), UNDERLINE, BOLD, (COLOR + '15,12'), UNDERLINE, BOLD, (COLOR + '12,12')))
    XC.command("say %s%s                                                " % (UNDERLINE, (COLOR + '12,12')))
    XC.command("say %s%s           %s%s%sPress any key to continue_%s%s%s           " % (UNDERLINE, (COLOR + '12,12'), UNDERLINE, BOLD, (COLOR + '15,12'), UNDERLINE, BOLD, (COLOR + '12,12')))
    XC.command("say %s%s                                                " % (UNDERLINE, (COLOR + '12,12')))
    XC.command("say %s%s                                                " % (UNDERLINE, (COLOR + '12,12')))
    XC.command("say %s%s                                                " % (UNDERLINE, (COLOR + '12,12')))
  except:
    print 'error'

XC.hook_command("bsod", bsod)
XC.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')
