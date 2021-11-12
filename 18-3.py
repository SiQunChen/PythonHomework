def one(b):
    for i in range(1,b+1):
        if i == 1:
            one_one(i)
        else:
            print("")
            one_one(i)
        
def one_one(i):
    back=2*i-1
    for j in range(1,2*i+1):
        if j>i:
            if back!=0:
                print(back,end="")
                back=back-1
        else:
            print(j,end="")
            back=back-1

def two(b):
    for i in range(1,b+1):   
        print("_"*int(b-i),end="")  
        two_one(i)
        print("_"*int(b-i),end="")
        print("")   

def two_one(i):
    back=2*i-1
    for j in range(1,2*i):
        if j>i:
            if back!=0:
                print(back,end="")
                back=back-1
        else:
            print(j,end="")
            back=back-1

def three(b):
    for i in range(b,0,-1):   
        print("_"*int(b-i),end="")  
        three_one(i,b)
        print("_"*int(b-i),end="")
        print("")

def three_one(i,b):
    back=2*i-1
    for j in range(1,2*i):
        if j>i:
            print(back,end="")
            back=back-1
        else:
            print(j,end="")
            back=back-1

def main():
    a=int(input())
    b=int(input())
    if a == 1:
        one(b)
    elif a == 2:
        two(b)
    elif a == 3:
        three(b)

main()