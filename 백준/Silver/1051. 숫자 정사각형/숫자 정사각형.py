import sys
N, M = map(int, input().split())
rect = [list(input().strip()) for _ in range(N)]

# 숫자는 0~9
# print(N, M)
# print(rect)

# 42101
# 22100
# 22101
# [0][2], [0][4]
# [2][2], [2][4]
res=0
len = min(N, M)
# print(len)



if len == 1:
    print(1)
    sys.exit()
      
elif len > 1:
        for i in range(M):
            for j in range(N):
                for l in range(1, len):
                    if j+l < N and i+l < M: 
                        a=rect[j][i] 
                        b=rect[j][i+l]
                        c=rect[j+l][i]
                        d=rect[j+l][i+l]
                        
                        if a == b == c == d:
                            res = max(res, (l+1) ** 2)

if res == 0:
    print(1)
else: print(res)
