def specify(temp,str):
    temp=temp.split(" ")
    #print(temp)
    if temp[0]=="ADD_W_FRONT":
        str[int(temp[1])-1].insert(int(temp[2])-1,temp[3])
    elif temp[0]=="ADD_W_AFTER":
        str[int(temp[1])-1].insert(int(temp[2]),temp[3])
    elif temp[0]=="ADD_S_FRONT":
        for i in range(len(temp)-1,1,-1):
            str[int(temp[1])-1].insert(0,temp[i])
    elif temp[0]=="ADD_S_AFTER":
        for i in range(2,len(temp)):
            str[int(temp[1])-1].append(temp[i])
    elif temp[0]=="INSERT_FRONT":
        for i in range(len(str)):
            z=0
            while z<len(str[i]):
                if  temp[1] in str[i][z]:
                    for j in range(2,len(temp)):
                        str[i].insert(z+j-2,temp[j])
                        z+=j
                else:
                    z+=1   
    elif temp[0]=="INSERT_AFTER":
        for i in range(len(str)):
            z=0
            while z<len(str[i]):
                if  temp[1] in str[i][z]:
                    for j in range(2,len(temp)):
                        str[i].insert(z+j-1,temp[j])
                        z+=j
                else:
                    z+=1 
    elif temp[0]=="DEL_W":
        #print(str[0])
        str[int(temp[1])-1].pop(int(temp[2])-1)
    elif temp[0]=="DEL_L":
            str.pop(int(temp[1])-1)
    elif temp[0]=="REPLACE":
        for i in range(len(str)):
            for j in range(len(str[i])):
                if str[i][j]==temp[1]:
                    x=str[i].pop(j)
                    x=temp[2]
                    str[i].insert(j,x)
    elif temp[0]=="COUNT":
        count=0
        for i in str:
                count+=len(i)
        print(count)
    return str

m,n=input().split(" ")
str=[]
com=[]
for i in range(int(m)):
    s=input().split(" ")
    str.append(s)
for i in range(int(n)):
    com.append(input())
while com:
    temp=com.pop(0)
    specify(temp,str)

for i in str:
    print(" ".join(i))