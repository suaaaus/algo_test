import sys
input = sys.stdin.readline

n = int(input())
numlist = list(map(int,input().split()))
x = int(input())

"""n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. 
ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, 
ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오."""

"""투포인터X, 완전탐색
cnt=0
for i in range(n):
    for j in range(i+1,n):
        if numlist[i]+numlist[j] == x:
            cnt+=1

print(cnt) """

#투포인터 방식은 정렬된 배열을 사용해, 양쪽에서 포인터를 움직이며 조건을 만족하는 쌍을 찾는 방식입니다.

numlist.sort()
#[1,2,3,5,7,9,10,11,12,15]
cnt=0
i,j = 0,n-1
while i < j:
    sum=numlist[i]+numlist[j]
    if sum > x:
        j-=1
    elif sum < x:
        i+=1
    elif sum == x:
        cnt+=1
        i+=1
        j-=1

print(cnt)