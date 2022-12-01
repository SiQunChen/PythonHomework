def judge(n):
    if n==1:
        return 2
    else:
        return judge(n-1)+n

def main():
    n=int(input())
    print(judge(n))

main()