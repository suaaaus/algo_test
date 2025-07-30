import sys
input = sys.stdin.readline

N, M = map(int, input().split())

setS = [input().strip() for _ in range(N)]
checklist = [input().strip() for _ in range(M)]

# print(N, M)
# print(setS)
# print(checklist)

res=0
for i in range (len(checklist)):
    if checklist[i] in setS:
        res+=1
        
print(res)