n1=input().split()
n2=input().split()
a1={}
s=-1
for i in n2:
    s+=1
    a1[i]=n1[s]
a2=sorted(a1.items(), key=lambda x:x[0])
for i in a2:
    print(i[1],end="")