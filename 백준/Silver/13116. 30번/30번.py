N = int(input())

# 트리에서 공통 부모 중 최댓값 찾는 문제
#print(A, B)


# 예제 출력
# 40
# 10
# 5110

# 33 /2 16--8--4
# 79/2  39--19--9--4


def solve_30(A, B): # 이진
    while A != B:
        if A > B:
            A //= 2
        else:
            B //= 2
    print(10 * A)
    
    
    
for i in range(N): 
    A, B = map(int,input().split())
    #print(A, B)    
    solve_30(A, B)


