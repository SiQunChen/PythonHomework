def sequence(n):
    arr=[0,1]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return 2*sequence(n-1)+3*sequence(n-2)

def main():
    n=float(input())
    if n<2 or n%1!=0:
        print("Error")
    else:
        print(sequence(int(n)))

main()