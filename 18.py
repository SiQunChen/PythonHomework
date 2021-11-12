def one(b):
    for i in range(1,b+1):
        if i == 1:
            one_one(b,i)
        else:
            print("")
            one_one(b,i)
        
def one_one(b,i):
    for j in range(1,i+1):
        print(j,end="")
        one_two(b,j,i)

def one_two(b,j,i):
    if j<i:
        pass
    else:
        for k in range(j-1,0,-1):
            print(k,end="")

def two(b):
    for i in range(b):   
        print("_"*int(b-1-i),end="")  
        two_one(i)
        two_two(i)
        print("_"*int(b-1-i),end="")
        print("")   

def two_one(i):
    for j in range(1,i+2):
        print(j,end="")

def two_two(i):
    for k in range(i,0,-1):
        print(k,end="")

def three(b):
    for i in range(b):   
        print("_"*i,end="")  
        three_one(i,b)
        three_two(i,b)
        print("_"*i,end="")
        print("")

def three_one(i,b):
    for j in range(1,int(b-i+1)):
        print(j,end="")

def three_two(i,b):
    for k in range(int(b-1-i),0,-1):
        print(k,end="") 

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