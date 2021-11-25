def abc(n,time):
    if n>=1 and n%2==0:
        time+=1
        n=n//2
        return abc(n,time)
    elif n>=2 and n%2==1:
        time+=1
        n=(n+1)//2
        return abc(n,time)
    else:
        return time
    

def main():
    n=[]
    ans=[]
    while 1:
        a=input()
        b=int(a,2)
        if a=="-1":
            break
        else:
            n.append(b)
    for i in range(len(n)):
        time=0
        ans.append("{0:b}".format(abc(n[i],time)))
    for i in ans:
        if len(list(i))==1:
            print("0"*3+i)
        elif len(list(i))==2:
            print("0"*2+i)
        elif len(list(i))==3:
            print("0"+i)
        else:
            print(i)
main()