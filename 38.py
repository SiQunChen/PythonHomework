n=input()
ans=set()
for i in range(len(n)+1):
    for j in range(i):
        if n[j:i]==n[j:i][::-1]:
            ans.add(n[j:i])
print("#".join(i for i in sorted(ans)))