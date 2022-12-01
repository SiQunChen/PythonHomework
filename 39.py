from itertools import combinations
n=input().split()
shit=list(combinations(list(n[0]),int(n[1])))
ans=[]
for i in range(len(shit)):
    x=""
    for j in range(len(shit[i])):
        x+=shit[i][j]
    ans.append(x)
for i in sorted(ans):
    print(f"{i} ",end="")