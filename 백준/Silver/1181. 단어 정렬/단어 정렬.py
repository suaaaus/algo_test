import sys
input = sys.stdin.readline

N = int(input())
word = [input().strip() for _ in range(N)]
new=list(set(word))
word2 = sorted(new, key=lambda x: (len(x), x))

for i in word2:
    print(i)