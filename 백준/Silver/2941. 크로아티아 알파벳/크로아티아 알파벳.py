word = list(str(input().strip()))


# 크로아티아 알파벳	변경
# č	              c=
# ć	              c-
# dž	          dz=
# đ	              d-
# lj	          lj
# nj	          nj
# š	              s=
# ž	              z=

calpha = 0

for i in range(len(word)):
    # c=, c-
    if word[i]=='c' and i < len(word)-1:
        if word[i+1]=='=' or word[i+1]=='-':
            calpha = calpha+1
    
    # dz=        
    if word[i]=='d' and i < len(word)-2:
        if word[i+1]=='z' and word[i+2]=='=':
            calpha = calpha+1
        
    # d- 
    if word[i]=='d' and i < len(word)-1:       
        if word[i+1]=='-' :
            calpha = calpha+1
 
    # word가 총 5글자면 idx는 0 1 2 3 4
    # len(word) = 5
    # len(word)-1 = 4
    if i < len(word)-1: # 맨 뒤 글자 아니면
        # lj, nj
        if (word[i]=='l' or word[i]=='n') and word[i+1]=='j' :
            calpha = calpha+1
        # s=, z=
        if (word[i]=='s' or word[i]=='z') and word[i+1]=='=' :
            calpha = calpha+1
        
          
    
# print(word) 
# print(calpha)   
print(len(word)-calpha)