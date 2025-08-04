N = int(input())
arrA = list(map(int, input().split()))
# [1, 2, 2, 1, 3] 이면

idxA = list(enumerate(arrA)) # idx 정보와 요소 값을 tuple로 저장하는 함수
# [(0, 1), (1, 2), (2, 2), (3, 1), (4, 3)]
sort_idxA= sorted(idxA, key=lambda x: (x[1], x[0])) # 값 오름차순 
# [(0, 1), (3, 1), (1, 2), (2, 2), (4, 3)]
idx = [i for i, _ in sort_idxA]
# [0, 3, 1, 2, 4]
# 답은  [0, 2, 3, 1, 4]  가 되어야만..

p_list = [0] * N
for (i, p) in enumerate(idx):
    p_list[p] = i

print(*p_list)

# 왜 안되는겨 젠장
# res=[-1] * (len(arrA))
# ori = 0
# for i in range(1, len(arrA)+1): # 1
#     for j in range(len(arrA)):
#         if arrA[j] == i:
#             res[j] = ori
#             ori += 1
# print(*res)      
