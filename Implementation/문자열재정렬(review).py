S = input()
alphabets = [str(tmp) for tmp in S if not tmp.isdigit()]
numbers = [int(tmp) for tmp in S if tmp.isdigit()]
alphabets = sorted(alphabets)
answer = alphabets + numbers
for i in answer:
  print(i, end='')
print()
