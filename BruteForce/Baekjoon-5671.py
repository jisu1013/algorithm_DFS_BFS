import sys

nums = []
for i in sys.stdin:
  nums.append(i)
  n,m = i.split()  
  cnt = 0
  for i in range(int(n),int(m)+1):
    tmp = list(str(i))
    if len(tmp) == len(list(set(tmp))):
      cnt += 1 
    #print(tmp)
  print(cnt)
