def judge(n,k):
    union=set()
    time=0
    for_time=0
    for i in range(n-1):
        for_time+=1
        if k[n-1]&k[i]!=set():
            time+=1
            for j in k[i]:
                union.add(j)
            for p in k[n-1]:
                union.add(p)
            if time==n-1:
                print(f"{min(union)},{max(union)}")
        else:
            if union==set():
                if for_time==n-1 and time==0:
                    print(f"{min(k[i])},{max(k[i])}")
                    print(f"{min(k[-1])},{max(k[-1])}")
                else:
                    print(f"{min(k[i])},{max(k[i])}")
            else:
                print(f"{min(union)},{max(union)}")
                print(f"{min(k[i])},{max(k[i])}")

def main():
    n=int(input())
    k=[]
    qua=set()
    for i in range(n):
        m=set()
        l=input()
        a=l.find(",")
        for j in range(int(l[:a]),int(l[a+1:])+1):
            m.add(j)
        k.append(m)
    if k[0]==k[1]:
        print(l)
    else:
        judge(n,k)

main()