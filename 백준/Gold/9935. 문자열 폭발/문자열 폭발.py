string = str(input())
bumb = list(str(input()))

# ###############시간초과#################
# while(bumb in string):
#     if (bumb in string):
#         new=string.replace(bumb,'')
#         string = new

# if (len(new)==0):
#     print('FRULA')
# else:
#     print(new)
# ######################################

word = []

for i in range(len(string)):
    word.append(string[i])
    if ((len(word)>=len(bumb)) and (word[-(len(bumb)):] == bumb[:])): ### 여기서 오류
        for j in range(len(bumb)):
            word.pop()
            
            
if (len(word)==0):
    print('FRULA')
else:
    print(*word,sep='')          

# i=5일때
# word[2:]인데 word[1]임
