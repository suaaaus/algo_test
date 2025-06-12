import sys
input = sys.stdin.readline

N = int(input())
lines = [list(input().strip()) for _ in range(N)]

# 3
# config.sys
# config.inf
# configures
# lines = [[c,o,n,f,i,g,.,s,y,s],[c,o,n,f,i,g,.,i,n,f],[]]

repeat = len(lines[0]) # 글자수만큼 반복
pattern = [] # 출력 문자자

for j in range(repeat):  
    char = lines[0][j]   # 비교할 문자자
    same = True
    for i in range(1, N):  
        if lines[i][j] != char:
            same = False
            break
    if same:
        pattern.append(char)
    else:
        pattern.append('?')

print(''.join(pattern))