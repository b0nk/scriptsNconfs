BOLD = '\002'
COLOR = '\003'
HIDDEN = '\010'
UNDERLINE = '\037'
ORIGINALCOLOR = '\017'
REVERSECOLOR = '\026'
BEEP = '\007'
ITALICS = '\035'

WHITE = '00'
BLACK = '01'
DBLUE = '02'
DGREEN = '03'
RED = '04'
DRED = '05'
PURPLE = '06'
ORANGE = '07'
YELLOW = '08'
GREEN = '09'
TEAL = '10'
CYAN = '11'
BLUE = '12'
PINK = '13'
GRAY = '14'
SILVER = '15'

ALLCOLORS = [WHITE, BLACK, DBLUE, DGREEN, RED, DRED, PURPLE, ORANGE, YELLOW, GREEN, TEAL, CYAN, BLUE, PINK, GRAY, SILVER]

def color1(c1, text):
  return "%s%s%s%s" % (COLOR, c1, text, COLOR)

def color2(c1, c2, text):
  return "%s%s,%s%s%s" % (COLOR, c1, c2, text, COLOR)

def boldtext(text):
  return "%s%s%s" % (BOLD, text, BOLD)

def underlineText(text):
  return "%s%s%s" % (UNDERLINE, text, UNDERLINE)

def italicText(text):
  return "%s%s%s" % (ITALICS, text, ITALICS)
