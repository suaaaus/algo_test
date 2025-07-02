import sys
input = sys.stdin.readline

N=int(input())
timetable = [tuple(map(int, input().split())) for _ in range(N)]

#아, 끝나는 시간이 빨라야지 최대한 많은 회의를 선택할 수 있구나.
timetable.sort(key=lambda x: (x[1], x[0]))
cnt=0
last_end_time=0

for start, end in timetable:
    if start >= last_end_time:
        cnt+=1
        last_end_time = end
print(cnt)

