N = int(input()) # <300
stairs = list((int(input()) for _ in range(N)))

#print(stairs)
# 1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 
#    즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 3. 마지막 도착 계단은 반드시 밟아야 한다.
# 1 2 3 4 5 6
# . .   .   . 75
# .   . .   . 70
# .   .   . . 55
#   . .   . . 75
#   .   .   . 65
# dynamic programming;;;;;;

score = [0] * N

for i in range(N): 
    if(i==0):
        score[0]=stairs[0]
    elif(i==1):
        score[1]= max(score[0]+stairs[1], stairs[1])
    elif(i==2):
        score[2]= stairs[2] + max(score[0], stairs[1])    
    elif(i>=3):
        score[i] = stairs[i] + max(stairs[i-1]+score[i-3], score[i-2])
                            # 한칸 건너뛴경우                   


print(score[N-1]) # N번쨰