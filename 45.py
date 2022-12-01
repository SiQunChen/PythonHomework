def add_route(x,y,route):
    if not x in route.keys():
        route[x]=[]
    route[x].append(y)
    return route
if __name__=='__main__':
    N,X,Y,Z = input().split()
    route={}
    for i in range(int(N)):
        x,y = input().split()
        route = add_route(x,y,route)
        route = add_route(y,x,route)
    print(route)
    cur=X
    a=[[X]]
    b=set()
    b.add(X)
    c={}
    time=0
    while True:
        for k in range(len(a)):
            b.add(j for i in route[a[0][k]] for j in i if not j in b)
            a.append([j for i in route[a[0][k]] for j in i if not j in b])
        a.pop(0)
        print(a,b)
        if time==0:
            for i in range(len(a[0])):
                c[i]=[]
                c[i].append(a[0][i])
        else:
            for i in range(len(a[0])):
                for j in range(len(c)):
                    c[j].append(a[i])
        print(c)
        for i in range(len(c)):
            for j in c[i]:
                if Y==j:
                    ans=c[i]
                    break
        time+=1
        if time==2:
            break