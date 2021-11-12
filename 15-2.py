n = int(input()) 
l = [int(input()) for _ in range(n)]
print(l)
temp=sorted(l)
print(temp)
print(temp[-2])
print(temp[0]*temp[-1])