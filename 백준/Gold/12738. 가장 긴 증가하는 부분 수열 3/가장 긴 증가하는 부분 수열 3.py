import sys
input = sys.stdin.readline
from bisect import bisect_left

N= int(input())
listA = list(map(int, input().split()))

#정렬안해도될듯
rs=[listA[0]]
for num in listA: 
    blft = bisect_left(rs, num)
    if len(rs) == blft:
          rs.append(num)
    else:
        rs[blft] = num

print(len(rs))