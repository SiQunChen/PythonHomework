def Fibonacci_number(n,data):
    if data[n]==0:
        data[n]=Fibonacci_number(n-1,data)+Fibonacci_number(n-2,data)
    return data[n]

def main():
    arr=[]
    while 1:
        n=input()
        if n=="-1":
            break
        else:
            n=int(n)
            arr.append(n)
    data=[1,1]+[0 for i in range(max(arr)-1)]
    for i in arr:
        print(Fibonacci_number(i-1,data))

main()