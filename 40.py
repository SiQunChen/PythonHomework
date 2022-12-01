n=input().split()
sen=""
for i in n[0]:
    if i.isupper():
        sen+=i.lower()
    elif i.islower():
        sen+=i.upper()
ans=[sen[i-int(n[1]):i] for i in range(int(n[1]),len(sen)+int(n[1]),int(n[1]))]
print("/".join(i for i in ans[::-1]))