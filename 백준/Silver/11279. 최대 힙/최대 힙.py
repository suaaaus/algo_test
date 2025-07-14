import heapq
import sys
input = sys.stdin.readline

N = int(input())

data = list(int(input()) for _ in range(N))

for i in range(N):
    data[i] = data[i]*(-1)

# print(data)

# 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
# x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 

# 13
# 0 --- 0
# 1 [1]
# 2 [1,2]
# 0 --- 2
# 0 --- 1
# 3 --- [3]
# 2 --- [3,2]
# 1 --- [3,2,1]
# 0 --- 3
# 0 --- 2
# 0 --- 1
# 0 --- 0
# 0 --- 0


dataheap =[]
heapq.heapify(dataheap)

rrr =[]
for i in range(N):
    if(data[i]!=0):
        heapq.heappush(dataheap, data[i])
        # print('append data:',dataheap)
    else:
        if (len(dataheap)>0):
            rrr.append(heapq.heappop(dataheap))
        else: 
            rrr.append(0)
            # print('heappop:',rrr)



for i in range(len(rrr)):
    rrr[i] = rrr[i]*(-1)

for i in range(len(rrr)):
    print(rrr[i])


