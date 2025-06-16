import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 세로N, 가로M
board = [list(input().strip()) for _ in range(N)]
# print(board)


diffW=[]
diffB=[]

# ex) N:10 M:13 에서       
# 가로 13에서 8개 6개 조합나옴
# 13-8+1 = 6
# 세로 10에서 8개 3개 조합나옴
# 10-8+1 = 3


# W로 시작
chessW = [[('W' if (i + j) % 2 == 0 else 'B') for j in range(8)] for i in range(8)]
# B로 시작
chessB = [[('B' if (i + j) % 2 == 0 else 'W') for j in range(8)] for i in range(8)]

def compare():
    differenceW = 0
    differenceB = 0
    for i in range(8):
            for j in range(8):
                if (chessW[i][j] != board[i+n][j+m]):
                    differenceW=differenceW+1
                if (chessB[i][j] != board[i+n][j+m]):
                    differenceB=differenceB+1
    diffW.append(differenceW)
    diffB.append(differenceB)


for n in range(N-7):
    for m in range(M-7):
        compare()

# print(diffW)
# print(diffB)

if (min(diffW)<min(diffB)):
    print(min(diffW))
else:
    print(min(diffB))

