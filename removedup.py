def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if x not in seen and not seen_add(x)]

array = [line for line in open('bl.p2p', 'r')]

array = f7(array)

with open("new.p2p", 'w') as f:
  for i in array:
    f.write(i)
f.close()
