def Greatest_common_factor(x,y):
    while x>0 and y>0:
        if x>y:
            x=x%y
        else:
            y=y%x
    return (x if x>y else y)
        

def main():
    arr=[]
    while 1:
        n=input()
        if n=="-1":
            break
        else:
            n=n.split()
            arr.append(n)
    for i in arr:
        first=Greatest_common_factor(int(i[0]),int(i[1]))
        print(Greatest_common_factor(first,int(i[2])))

main()