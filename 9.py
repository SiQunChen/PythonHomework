x=int(input())
y=int(input())
z=int(input())
if x<=10:
    appleprice=30*x
elif x>10 and x<=15:
    appleprice=30*0.95*x
elif x>15 and x<=20:
    appleprice=30*0.9*x
else:
    appleprice=30*0.8*x
if y<=10:
    kiwisprice=70*y
elif y>10 and y<=15:
    kiwisprice=70*0.9*y
elif y>15 and y<=20:
    kiwisprice=70*0.85*y
else:
    kiwisprice=70*0.75*y
if z<=10:
    pineappleprice=40*z
elif z>10 and z<=15:
    pineappleprice=40*0.85*z
elif z>15 and z<=20:
    pineappleprice=40*0.8*z
else:
    pineappleprice=40*0.8*z
if x+y+z>=30:
    total=(appleprice+kiwisprice+pineappleprice)*0.87
else:
    total=appleprice+kiwisprice+pineappleprice
print(int(total))
    
    
