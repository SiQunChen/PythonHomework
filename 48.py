def best(data,seq,time,first):
    all={1,2,3,4,5,6,7,8,9}
    seq_set=set()
    for i in seq:
        seq_set.add(int(i))
    find_0=all^seq_set
    first=int(first)
    for i in find_0:#判斷自己可不可以贏
        if (first==1 and len(seq)%2==0) or (first==2 and len(seq)%2==1):
            data[(int(i)-1)//3][int(i)%3-1]=1
            if check(data,seq,time,first)=="Computer win" or check(data,seq,time,first)=="Player win":
                return i
            else:
                data[(int(i)-1)//3][int(i)%3-1]=0
        elif (first==2 and len(seq)%2==0) or (first==1 and len(seq)%2==1):
            data[(int(i)-1)//3][int(i)%3-1]=2
            if check(data,seq,time,first)=="Computer win" or check(data,seq,time,first)=="Player win":
                return i
            else:
                data[(int(i)-1)//3][int(i)%3-1]=0
    for i in find_0:#判斷可不可以阻擋對手
        data[(int(i)-1)//3][int(i)%3-1]=1
        if check(data,seq,time,first)=="Computer win" or check(data,seq,time,first)=="Player win":
            return i
        else:
            data[(int(i)-1)//3][int(i)%3-1]=0
        data[(int(i)-1)//3][int(i)%3-1]=2
        if check(data,seq,time,first)=="Computer win" or check(data,seq,time,first)=="Player win":
            return i
        else:
            data[(int(i)-1)//3][int(i)%3-1]=0

def check(data,seq,time,first):
    time+=1
    for i in range(3):
        if data[i][i%3]==data[i][(i+1)%3]==data[i][(i+2)%3]==2 or data[i%3][i]==data[(i+1)%3][i]==data[(i+2)%3][i]==2:
            return "Computer win"
        elif data[i][i%3]==data[i][(i+1)%3]==data[i][(i+2)%3]==1 or data[i%3][i]==data[(i+1)%3][i]==data[(i+2)%3][i]==1:
            return "Player win"
        elif i==0 or i==2:
            if data[i%3][i%3]==data[(i+1)%3][(i+1)%3]==data[(i+2)%3][(i+2)%3]==1 or data[(i+2)%3][i%3]==data[(i+1)%3][(i+1)%3]==data[i%3][(i+2)%3]==1:
                return "Player win"
            elif data[i%3][i%3]==data[(i+1)%3][(i+1)%3]==data[(i+2)%3][(i+2)%3]==2 or data[(i+2)%3][i%3]==data[(i+1)%3][(i+1)%3]==data[i%3][(i+2)%3]==2:
                return "Computer win"
        elif len(seq)==9:
            return "Tie"
    if time==1:
        print("Undecided")
        return best(data,seq,time,first)

def game(first,seq,data,time):
    rep=0
    for i in range(1,len(seq)+1):
        j=i
        j+=rep
        time=2
        if data[(int(seq[i-1])-1)//3][int(seq[i-1])%3-1]==0:
            if first=='1':
                if j%2==1:
                    data[(int(seq[i-1])-1)//3][int(seq[i-1])%3-1]=1
                else:
                    data[(int(seq[i-1])-1)//3][int(seq[i-1])%3-1]=2
            else:
                if j%2==1:
                    data[(int(seq[i-1])-1)//3][int(seq[i-1])%3-1]=2
                else:
                    data[(int(seq[i-1])-1)//3][int(seq[i-1])%3-1]=1
        else:
            rep+=1
        if check(data,seq,time,first)=="Computer win" or check(data,seq,time,first)=="Player win":
            print("OK" if rep==0 else "Error")
            return data
    print("OK" if rep==0 else "Error")
    return data

if __name__=='__main__':
    first=str(input())
    seq=input().split()
    if (first=="1" or first=="2"):
        data=[[0]*3 for i in range(3)]
        time=0
        for i in game(first,seq,data,time):
            for j in i:
                print(f"{j} ",end="")
            print("")
        time=0
        print(check(data,seq,time,first))
    else:
        print("Error")