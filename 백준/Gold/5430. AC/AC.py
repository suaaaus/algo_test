import sys
import ast
input = sys.stdin.readline

def drlist(p_func):
    Dcount = 0
    Rcount = 0
    DRlist = []
    
    for i in range(len(p_func)):
        now = p_func[i]
        if now == 'R':
            if Dcount > 0:
                DRlist.append(Dcount) # 일단 추가
                Dcount = 0
            Rcount += 1
        else:  # 'D'
            if Rcount > 0:
                DRlist.append(Rcount)
                Rcount = 0
            Dcount += 1

    # 마지막 문자
    if Rcount > 0:
        DRlist.append(Rcount)
    if Dcount > 0:
        DRlist.append(Dcount)

    return DRlist

def solve_AC(p_func, DRlist, xlist):
    reversed = False
    for i in range(len(DRlist)): # DRlist순회[]
        if p_func[0] == 'R': # 처음이 R이면
            if i % 2 == 0:
                idx = 'R'# index짝수번째 R
            else:
                idx = 'D'
        else:  # 처음이 'D'
            if i % 2 == 0:
                idx = 'D'
            else:
                idx = 'R'

        if idx == 'R':
            if DRlist[i] % 2 == 1:
                reversed = not reversed
        else:  # D
            if DRlist[i] > len(xlist):
                print('error')
                return
            if not reversed:
                del xlist[:DRlist[i]]
            else:
                del xlist[-DRlist[i]:]

    if reversed:
        xlist.reverse() # reverse 최소화...

    print('[' + ','.join(map(str, xlist)) + ']') # 출력 형식 맞추기


T = int(input())
for _ in range(T): # T 개의 묶음
    p_func = list(input().strip()) # RDD
    n = int(input())
    xlist = ast.literal_eval(input()) # 리스트 형태 그대로 저장
    
    DRlist = drlist(p_func) # [1,2]
    solve_AC(p_func, DRlist, xlist)
