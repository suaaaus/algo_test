import math
N=int(input())

fac = str(math.factorial(N))
cnt = 0

for i in range(1, len(fac)):
    a = fac[-i]
    if(fac[-i]=='0'):
        cnt+=1
    else: break
    
print(cnt)