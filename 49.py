if __name__=='__main__':
    M,N=input().split()
    line=[]
    for i in range(int(M)):
        line.append(input().split())
    for i in range(int(N)):
        com=input().split()
        if com[0]=="ADD_W_FRONT":
            line[int(com[1])-1].insert(int(com[2])-1,com[3])
        elif com[0]=="ADD_W_AFTER":
            line[int(com[1])-1].insert(int(com[2]),com[3])
        elif com[0]=="ADD_S_FRONT":
            for i in range(2,len(com)):
                line[int(com[1])-1].insert(0,com[i])
        elif com[0]=="ADD_S_AFTER":
            add=[]
            for i in range(2,len(com)):
                add.append(com[i])
            line[int(com[1])-1].extend(add)
        elif com[0]=="INSERT_FRONT":
            l=[]
            w=[]
            for i in range(len(line)):
                for j in range(len(line[i])):
                    if line[i][j]==com[1]:
                        l.append(i)
                        w.append(j)
            for i in range(len(l)):
                line[int(l[i])].insert(int(w[i]),com[2])
        elif com[0]=="INSERT_AFTER":
            l=[]
            w=[]
            for i in range(len(line)):
                for j in range(len(line[i])):
                    if line[i][j]==com[1]:
                        l.append(i)
                        w.append(j)
            for i in range(len(l)):
                line[int(l[i])].insert(int(w[i])+1,com[2])
        elif com[0]=="DEL_W":
            line[int(com[1])-1].pop(int(com[2])-1)
        elif com[0]=="DEL_L":
            line.pop(int(com[1])-1)
        elif com[0]=="REPLACE":
            for i in range(len(line)):
                for j in range(len(line[i])):
                    if line[i][j]==com[1]:
                        line[i].pop(j)
                        line[i].insert(j,com[2])
        elif com[0]=="COPY_L":
            copy=line[int(com[1])-1].copy()
        elif com[0]=="COPY":
            copy=[line[int(com[1])-1][int(com[2])-1]].copy()
        elif com[0]=="PASTE_FRONT":
            for i in copy[::-1]:
                line[int(com[1])-1].insert(int(com[2])-1,i)
        elif com[0]=="PASTE_AFTER":
            for i in copy[::-1]:
                line[int(com[1])-1].insert(int(com[2]),i)
        else:
            count=0
            for i in range(len(line)):
                count+=len(line[i])
            print(count)
    for i in line:
        for j in i:
            print(j,end=" ")
        print("")