def main():
    n=int(input())
    if n==2:
        print(f"{n} is prime number")
    elif n>2 and n%2==0:
        print(f"{n} is not prime number")
    else:
        for i in range(3,int(n/2+1),2):
            if n%i==0:
                print(f"{n} is not prime number")
                break
        if i!=int(n/2):
            i=i+1
        if i==int(n/2):
            print(f"{n} is prime number")

main()