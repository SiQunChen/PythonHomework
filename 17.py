def one(b):
    for i in range(1,int(b/2+1)):
        print("*"*i)
    for j in range(int(b/2+1),0,-1):
        print("*"*j)

def two(b):
    for i in range(int(b/2),0,-1):
        print("."*i,end="")
        print("*"*(int(b/2-i+1)))
    for k in range(int(b/2+1)):
        print("."*k,end="")
        print("*"*(int(b/2-k+1)))

def three(b):
    for i in range(int((b-1)/2),0,-1):
        print("."*i,end="")
        print("*"*int(b-i*2))
    for k in range(0,int(b/2+1)):
        print("."*k,end="")
        print("*"*int(b-k*2))

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