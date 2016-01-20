import os
import sys

### Use dictionary to store respectively the departure and destination urls
### as the key-value pairs
url_dict = {}
while True:
  line = sys.stdin.readline()
  if len(line) == 0:
    break
  urls = line.split()
  if urls[0] != urls[2]:
    url_dict[urls[0]] = urls[2]

trace = [sys.argv[1]]
url = url_dict.get(sys.argv[1])

while url != "[none]":
  trace.append(url)
  url = url_dict.get(url)

i = 1
for url in reversed(trace):
  print '%d.'%i, url
  i += 1
