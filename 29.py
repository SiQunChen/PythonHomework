n=input().split()
for i in range(len(n)):
    n[i]=int(n[i])
m=sorted(n)
answer=[]
for i in range(len(m)):
    m[i]=int(m[i])
    if m[i]%2==1:
        answer.append(m[i])
for i in range(len(m)-1,-1,-1):
    if m[i]%2==0:
        answer.append(m[i])
print(answer)