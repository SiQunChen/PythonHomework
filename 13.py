def main():
    m=int(input())
    n=int(input())
    sum=0
    product=1
    for i in range(m,n+1,2):
        sum=sum+i
    for j in range(m,n+1,3):
        product=product*j
    print(sum)
    print(product)
main()