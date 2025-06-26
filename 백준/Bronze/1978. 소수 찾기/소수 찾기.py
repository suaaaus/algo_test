n = int(input())
num = list(map(int, input().split()))

res = 0  # 소수 개수

for i in range(n):
    q = num[i]
    if q < 2: # 1 건너뛰고
        continue
    cnt = 0  # 각 수 마다 초기화
    for j in range(2, q):
        if q % j != 0: # 0으로 안나눠지면
            cnt += 1
    if cnt == q - 2: 
        res += 1 # 소수

print(res)
