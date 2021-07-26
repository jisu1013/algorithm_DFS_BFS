N = int(input())
mountains = list(map(int,input().split()))
cnt = 0
for i in range(N):
    tmp = 0
    for j in range(i+1, N):
        if mountains[i] < mountains[j]:
            break
        else:
            tmp += 1
    cnt = max(tmp, cnt)
print(cnt)
