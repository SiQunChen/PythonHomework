def main():
    N=int(input())
    number=int(input())
    maxvalue=second=minvalue=number
    for i in range(N-1):
        number=int(input())
        if number>maxvalue:
            second=maxvalue
            maxvalue=number
        if number<minvalue:
            minvalue=number
    print(second)
    print(maxvalue*minvalue)

main()