# N과 L이 주어질 때, 합이 N이면서, 길이가 적어도 L인 가장 짧은 연속된 정수 리스트

# 만약 리스트의 길이가 100보다 작거나 같으면, 연속된 수를 첫째 줄에 공백으로 구분하여 출력한다. 
# 만약 길이가 100보다 크거나 그러한 수열이 없을 때는 -1을 출력한다.

N, L = map(int, input().split())

# 만약 길이가 2인게 있으면
# 9 10 => 19 안되고
# 18// (L+1) = 6 5 7 == 18 가능

# L = 4
# 18 // L = 4
# 3 4 5 6?


# 18 // 5 
# 3
# 1 2 3 4 5 
# 6+6+3=15

# 18 // 6
# 1 2 3 4 5 6 =21

# 20 커지면
# 안돼
def findnum(N, L):
    while(2<= L <= 100):
        quo = N // L
        if (L%2==0): #짝수면
            if (quo+1+quo)*(L//2) == N:
                return quo, L
            elif (quo+1+quo)*(L//2)>N:
                L += 1
                continue
            else:
                L += 1
        else: # 홀수면
            if quo*L == N:
                return quo, L
            elif quo*L > N:
                L += 1
                continue
            else:
                L += 1
        
        if quo < 2:
            break
        
    return None, None

        
        
        
quoe, Len = findnum(N, L)


if quoe is None or Len is None:
    print(-1)
else: 
    if Len%2 == 0:
        a = quoe - (Len//2 - 1)
    else:
        a = quoe - Len//2
        
    res = []
    for i in range(Len):
        if a < 0 :
            print(-1)
            break
        res.append(a)
        a+=1
        
    print(*res)