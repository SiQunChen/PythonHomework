def Fibonacci_number(n):
    data=[1,1]
    if n==1 or n==2:
        return 1
    else:
        return Fibonacci_number(n-1)+Fibonacci_number(n-2)

def main():
    arr=[]
    while 1:
        n=input()
        if n=="-1":
            break
        else:
            n=int(n)
            arr.append(n)
    for i in arr:
        print(Fibonacci_number(i))

main()