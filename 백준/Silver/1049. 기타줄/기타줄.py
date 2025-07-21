import sys
input = sys.stdin.readline

N, M = map(int, input().split())

strings = [list(map(int, input().split())) for _ in range(M)]


#세트
strings0 = sorted(strings, key = lambda x : x[0])
#낱개
strings1 = sorted(strings, key = lambda x : x[1])

# 세트만
def set(s0):
    return (N//6+1)*s0[0][0]
# 낱개만
def single(s1):
    return (N * s1[0][1])
# 세트 + 낱개
def set_single(s0, s1):
    return (N//6)*s0[0][0] + (N%6)*s1[0][1]

a = set(strings0)
b = single(strings1)
c = set_single(strings0, strings1)

print(min(a, b, c))