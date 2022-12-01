def add_edge(x,y,graph):
    if not x in graph.keys():
        graph[x]=[]
    graph[x].append(y)
    return graph
if __name__=='__main__':
    N,X,Y = input().split()
    graph = {}
    graph[X]=[]
    graph[Y]=[]
    for i in range(int(N)):
        x,y = input().split()
        graph = add_edge(x,y,graph)
        graph = add_edge(y,x,graph)
    vis = set()
    now = X
    flag = False
    que = []
    vis.add(X)
    while True:
        if now == Y:
            flag = True
        for v in graph[now]:
            if not v in vis:
                vis.add(v)
                que.append(v)
        if not que :
            break
        now = que.pop(0)
    if flag :
        print('Yes!')
    else :
        print('No!')