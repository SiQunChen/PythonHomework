if __name__=='__main__':
    N = int(input())
    uni = []
    for i in range(N):
        tmp = input().split()
        uni.append([tmp[0],set(pr for pr in tmp[1:]),0])
    req = input().split('+')
    for q in req :
        lst = q.split()
        for i,sch in enumerate(uni) :
            flag = True 
            for cond in lst:    
                if cond[0] == '!':
                    if cond[1:] in sch[1] :
                        flag = False
                else :
                    if not cond in sch[1]:
                        flag = False
            if flag :
                uni[i][2]+=1
    uni.sort (key = lambda x : x[2] ,reverse = True)
    for i,sch in enumerate(uni):
        if sch[2]!=0:
            print(f"{' ' if i!=0 else ''}{sch[0]},{sch[2]}",end='')