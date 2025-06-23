N = int(input())

# 2 : -1

# 3 : /3
# 4 : -1,/3
# 5 : -1,-1,/3 or -1, /2, /2

# 6 : /3,-1 or /2,/3
# 7 : -1, /2, /3 or -1, /3, -1
# 8 : /2, /2, -1 or -1,(#7)

# 9 : /3, /3
# 10 : -1, /3, /3 .......... dynamic programming

    
an = [0] * (N+1) # index 라 +1

# 점화식
for i in range(2,N+1):
    an[i] = an[i-1] + 1
    
    if (i % 3 == 0):
        an[i] = min(an[i//3]+1, an[i])
        
    if (i % 2 == 0):
        an[i] = min(an[i//2]+1, an[i])
        
        
print(an[N])