N = int(input())

# 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 
# 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

quo = N // 5
# ex) N = 19
#     quo = 3
chk = True
while (quo >= 0):
    if ((N - quo*5) % 3 == 0):
        print(((N - quo*5) // 3) + quo)
        chk = False
        break
    else: quo -= 1

    # 19 - 15 = 4

if (chk):
    print(-1)



        
    