def main():
    password=[]
    scores={}
    number={}
    near={}
    for i in range(30):
        a=input()
        if a=="-1":
            break
        else:
            password.append(a)
    for i in password:
        k=list(i)
        scores[i]=0
        number[i]=0
        near[i]=0
        for j in range(len(i)):
            if k[j].isupper():
                scores[i]+=2
            elif k[j].islower():
                scores[i]+=1
            elif k[j].isdigit():
                scores[i]+=3
                number[i]+=1
                if j!=len(i)-1:
                    if k[j+1].isdigit():
                        near[i]=0
                    else:
                        near[i]+=1
                else:
                    if k[len(i)-2].isdigit():
                        near[i]=0
                    else:
                        near[i]+=1
            elif k[j]=="~"or "!" or "@" or "#" or "$" or "%" or "^" or "&" or "*" or "<" or ">" or "_" or "+" or "=":
                scores[i]+=5
        print(number.get(i),near.get(i))
        if int(number.get(i))>=5 and near.get(i)==number.get(i):
            scores[i]+=10
    compare=sorted(scores.items(), key=lambda x:x[1])
    max=compare[-1]
    min=compare[0]
    print(compare)
    print(f"{max[0]} {max[1]}")
    print(f"{min[0]} {min[1]}")

main()