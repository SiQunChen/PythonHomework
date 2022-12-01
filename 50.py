def isConflict(m1,m2):
    if m1[2]==m2[2]:
        return True
    elif m1[2]>m2[2]:
        return isConflict(m2,m1)
    return m2[1]<m1[2]



def dfs(meets,now,rooms):

    if now == len(meets):
        return 0
    ans = 0
    
    
    for i in range(len(rooms)):
        temp=[]
        for m in rooms[i]:
                if isConflict(meets[now],m):
                    break
        else:
            if meets[now][0]<=peo[i][0]:
                rooms[i].append(meets[now])
                for next in range(now+1,len(meets)+1):
                    t = dfs(meets,next,rooms) + meets[now][2]-meets[now][1]
                    
                    ans = max(ans,t)
                rooms[i].remove(meets[now])
    return ans

peo=[]
def main():
    n,m = [int(i) for i in input().split()]
    
    meets = []
    for i in range(n):
        peo.append([int(i) for i in input().split()[1:]])
        
    for _ in range(m):
        meets.append([int(i) for i in input().split()[1:]])
    
    rooms = [[] for _ in range(n)]
    
    ans = 0
    for i in range(m):
        t = dfs(meets,i,rooms)
        ans = max(ans,t)
    print(ans)

main()