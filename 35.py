def judge(n):
    for i in range(len(n)):
        m=[]
        if n[i]=='[':
            for j in range(1,5):
                if n[i+j]!=']':
                    m.append(n[i+j])
                elif n[i+j]=='[':
                    return judge(n[i+j])
                else:
                    break
            print(int(n[i-1])*("".join(m)),end="")

def main():
    n=list(input())
    judge(n)

main()