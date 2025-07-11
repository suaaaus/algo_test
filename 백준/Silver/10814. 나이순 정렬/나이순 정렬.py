N = int(input())
member = [input().split() for _ in range(N)]
#print(member)
member = [[int(age), name] for age, name in member]
#print(member)
sorted_age = sorted(member, key=lambda x: x[0])
#print(member)


# 나이 같으면 입력한 순 
for i in range(N):
    print(*sorted_age[i])

