n = int(input())

# cnt = 0
# # fibonacci
# def fib_recur(n):
#     global cnt
#     if (n==1 or n==2):
#         cnt+=1
#         return 1
#     else:
#         res = fib_recur(n-1)+fib_recur(n-2)
#         # cnt+=1
#         return (cnt) ##### 시간초과

# dynamic programming
# def fib_dp(n):
#     f=[1,1]
#     for i in range(2, n+1):
#         f.append(f[i-1] + f[i-2])
#     # return f[n]
#     return i-1 # 횟수 출력 이니까


fibo = [0] * (n+1)
fibo[1] = fibo[2] = 1
for i in range(3,n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

# res2 = fib_dp(n-1) # idx기준 n-1
print(fibo[n], n-2) # 값 말고 횟수