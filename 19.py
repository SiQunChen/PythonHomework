def my_print(n):
    for i in range(n):
        if i==0:
            print("#"*(i+n),end="")
            for k in range(n,0,-1):
                print(k,end="")
        else:
            print("")
            print("#"*(i+n),end="")
            for k in range(n-i,0,-1):
                print(k,end="")

def main():
    n=int(input())
    my_print(n)

main()