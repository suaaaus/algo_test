import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

num.sort()
# [-99, -2, -1, 4, 98]

#     # idx는 0부터.. N-1까지 있음
#     min = num[i] + num[N-1-i]
start = 0
end = N-1


min_val = abs(num[start] + num[end])
min_idx = (start, end)  

while(start < end):
    mix = num[start]+num[end]

    if abs(mix) < min_val:
        min_val = abs(mix) # 갱신
        min_idx = (start, end)
        if min_val == 0:
            break
    
    if mix < 0:
        start += 1
    else:
        end -= 1


a, b = min_idx 
print(num[a], num[b])