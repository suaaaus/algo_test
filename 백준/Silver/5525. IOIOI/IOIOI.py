from collections import deque

N = int(input())
M = int(input())
S = input()


discover_Pn = []

def find_Pn(N, M, S):
    global discover_Pn
    i = 0
    count = 0  # IOI 반복 횟수
    
    while (i < M - 1):
        if S[i] == 'I' and i + 2 < M and S[i+1] == 'O' and S[i+2] == 'I':
            count += 1
            i += 2 # idx건너뜀
            if count >= N:
                discover_Pn.append(2 * N + 1)  # Pn 길이 저장
        else:
            count = 0
            i += 1

find_Pn(N, M, S)
# ㅠㅠ numpy 못씀
# np_Pn = np.array(discover_Pn)
# m = (np_Pn - 1) // 2 # m은 찾은 Pn의 n값 배열
# nn = m - N + 1       # nn은 그 Pn 배열에 N이 몇변 들어가는지
# print(np.sum(nn))    # 의 합


total = 0
for pn in discover_Pn: # discover_Pn은 S안에 Pn이 몇글자로 존재하는지
    # ex) OOIOIOOIOI 는 [3,3]
    # 이걸 왜 구하냐믄.. P7에 P3은 7-3 +1개 있음 
    m = (pn - 1) // 2
    nn = m - N + 1
    if nn > 0:
        total += nn

print(total)