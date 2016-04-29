from os import listdir
from os.path import isfile, join

old = raw_input('Replace: ')
new = raw_input('With: ')

# old = 'Left\x94ver'
# new = 'Left\xf6ver'

onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]

for i in onlyfiles:
  if not i.endswith('.py'):
    f = open(i, 'r')
    content = f.read()
    f.close()
    if(old in content):
      f = open(i, 'w')
      print 'found in %s' % i
      content = content.replace(old, new)
      f.write(content)
      f.close()

print 'done'
raw_input()
