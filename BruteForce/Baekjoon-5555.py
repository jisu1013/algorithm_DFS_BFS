target = input()
result = 0
N = int(input())
for i in range(N):
  ring = input()
  for j in range(10):
    start = j
    end = j + len(target)
    if end > 10:
      end -= 10
      tmp = ring[start:]+ring[:end]
      #print(start,end,ring[start:]+ring[:end])
      if tmp == target:
        result += 1
        break
    else:
      if ring[start:end] == target:
        result += 1
        break
      #print(start,end,ring[start:end])
print(result)
