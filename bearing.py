from sys import argv

directions = ["N", "NNW", "NW", "WNW", "W", "WSW", "SW", "SSW",
              "S", "SSE", "SE", "ESE", "E", "ENE", "NE", "NNE"]
try:
  bear = int(argv[1])
except (IndexError, ValueError):
  print "Usage: %s <int>" % argv[0]
  exit(1)

deg = int(bear / (360 / len(directions)))
print directions[deg % 16]
