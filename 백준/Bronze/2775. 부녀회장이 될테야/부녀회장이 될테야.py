import sys
input = sys.stdin.readline
T = int(input())


# apt = [[0]*n]*(k+1) // 같은 list객체가 됨.. 안됨!!!
# apt = [[0]*n for _ in range(k+1)] # 이렇게 해야됨

global apt

def solve_dp(k, n):  
    global apt
    for i in range(1,k+1): # 1층부터 .. k층 n호 구하기. i=k
        for j in range(n+1): # j는 n
            if (j==0): # 1호에는 무조건 1
                apt[i][0] = 1
            elif (j>0): # 2호부터는 점화식
                apt[i][j]=apt[i-1][j]+apt[i][j-1]
    print(apt[k][n-1])


apt = [[0]*(14+1) for _ in range(14+1)] # 배열 만들기
# 0 층 생성
for i in range(14):
    apt[0][i] = i+1 
# apt 생성 -------    
   
for _ in range(T):
    k = int(input())
    n = int(input())
    # T개의 경우마다 
    solve_dp(k,n)