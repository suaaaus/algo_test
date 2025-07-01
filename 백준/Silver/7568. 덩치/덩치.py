# 2 ≤ N ≤ 50
# 10 ≤ x, y ≤ 200
# (kg, cm)
# (x, y), (p, q)라고 할 때 (x > p && y > q)


N = int(input())
kgcm = [list(map(int, input().split())) for _ in range(N)]

rs=[1]* N

for i in range(N):
    for j in range(N):
        if (kgcm[i][0] < kgcm[j][0] and kgcm[i][1] < kgcm[j][1]):
            rs[i]+=1
print(*rs)