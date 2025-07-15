# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다. 
A, B = map(int, input().split())

# A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

# 40021 /100 = 400
# 100 
# 4002
# 2001 200
# 100

cal = 1

while(B > A):

    if (B % 10 == 1):
        B -= 1
        B = B//10
        cal += 1
    elif (B % 2 == 0):
        B = B//2
        cal += 1
    else: break

if (B == A):
    print(cal)

else:
    print(-1)


