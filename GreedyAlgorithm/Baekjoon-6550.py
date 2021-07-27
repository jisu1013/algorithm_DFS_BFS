import sys

while True:
  line = sys.stdin.readline().strip()
  if not line:
    break
  s,t = line.split()
  index = 0
  for letter in t:
    if letter == s[index]:
      index += 1
    if index == len(s):
      break
  if index == len(s):
    print('Yes')
  else:
    print('No')
