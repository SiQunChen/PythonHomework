def lower(z):
    sum=0
    for j in z:
        if j.islower():
            sum=sum+1
            print(j,end="")
        else:
            pass
    if sum==0:
        print("No lowercase letters")
    else:
        pass

def many(y):
    number=len(y)
    return number

def upmany(x):
    cc=0
    for i in x:
        if i.isupper():
            cc=cc+1
        else:
            pass
    return cc

def main():
    sentence=str(input())
    lower(sentence)
    print("")
    print(many(sentence))
    print(upmany(sentence))
main()