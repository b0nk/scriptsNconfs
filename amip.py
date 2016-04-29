# AMIP test
# %s || %1 - %2 - %4 || %fpath\cover.jpg
from Tkinter import *

next = ''


def update(main, current):

  global next

  format = '''%s - %s
  [%s]'''
  with open('amip.txt', 'r') as f:
    next = f.readline()

    info = next.split(" || ")[1].split(" - ", 2)
    artist = info[0]
    title = info[1]
    albumInfo = info[2].split(" ||")[0]

    next = format % (artist, title, albumInfo)

    if current.get() != next:
      current.set(next)

  f.close()
  main.after(100, lambda: update(main, current))

main = Tk()

current = StringVar()

main.title('')

label = Label(main,
              textvariable=current,
              bg="#000",
              fg="#F80",
              anchor="n",
              font=("Calibri", 28, "bold"),
              width = 71,
              bd = 0,
              justify = "center")

label.pack()

update(main, current)

main.mainloop()
