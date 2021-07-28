import sys

sentence = []
line = sys.stdin.readline().strip()  
sentence = line.split()
answer = ['U','C','P','C']
index = 0
for word in sentence:
  for letter in word:
    if index == 4:
      break
    if letter == answer[index]:
      index += 1
if index == 4:
  print('I love UCPC')
else:
  print('I hate UCPC') 
