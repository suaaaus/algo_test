N = int(input())

# 666     1
# 1666    2 ...

end_num = 665
cnt = 0

# if 25666
def is_endnum():
    global cnt
    global end_num

    # in 은 int 말고 str에서
    if ('666' in str(end_num)):
        cnt+=1

while(1): 
    end_num += 1
    is_endnum()
    
    if (cnt == N):
        break
        
print(end_num)

