def add(x,y,s):
    if not x in s.keys():
        s[x]=[]
    s[x].append(y)
    return s

def findpath(s,node,path,target):
    while(len(node)!=0):
        temp=node.pop(0)
        newpath=path.pop(0)+[temp]

        if temp==target:
            return newpath
        
        for i in s[temp]:
            if i not in newpath and i not in node:
                node.append(i)
                path.append(newpath)
    return[]

N,X,Y,Z=input().split()
N=int(N)
s={}
times=1
for i in range(N):
    x,y=input().split()
    add(x,y,s)
    add(y,x,s)
#print(s)

path_1=findpath(s,[X],[[]],Y)
#print("------------------")
path_2=findpath(s,[Y],[[]],Z)
#print(path_1,path_2)

if not path_1 or not path_2:
    print("No way!")
else:
    print(len(path_1+path_2[1::])-1)
    print("-".join(path_1+path_2[1::]))