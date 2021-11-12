def main():
    a=int(input())
    b=int(input())
    if a%2==1:
        a=a+1
    if b%2==0:
        b=b+1
    print(sum(range(a,b,2)))

main()