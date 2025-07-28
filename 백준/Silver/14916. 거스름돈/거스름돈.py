# 거스름돈 동전의 최소 개수를 출력한다. 만약 거슬러 줄 수 없으면 -1을 출력한다.
# 2원짜리 동전과 5원짜리 동전은 무한정 많이 가지고 있다. 
N = int(input())
# n(1 ≤ n ≤ 100,000)


dp = [-1] * (N + 1) # 일단 -1
dp[0] = 0  # 0원 0개

for i in range(1, N + 1):
    if (i >= 2 and dp[i - 2] != -1):
        dp[i] = dp[i - 2] + 1
    if (i >= 5 and dp[i - 5] != -1):
        if (dp[i] == -1):
            dp[i] = dp[i - 5] + 1
        else:
            dp[i] = min(dp[i], dp[i - 5] + 1)

print(dp[N])
