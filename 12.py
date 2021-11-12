a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
Type183=int(a*0.08+b*0.1393+c*0.1349+d*1.1287+e*1.4803)
Type383=int(a*0.07+b*0.1304+c*0.1217+d*1.1127+e*1.2458)
Type983=int(a*0.06+b*0.1087+c*0.1018+d*0.9572+e*1.1243)
if Type183<183:
    Type183=183
else:
    pass
if Type383<383:
    Type383=383
else:
    pass
if Type983<983:
    Type983=983
else:
    pass
if Type183<Type383 and Type183<Type983:
    print("Type 183")
elif Type383<Type183 and Type383<Type983:
    print("Type 383")
else:
    print("Type 983")

    
