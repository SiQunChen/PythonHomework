arr=input().split(" ")
stack=[];stack2=[]
f=""
for i in arr:
    s=i
    if f=="*":
        s=str(float(temp)*float(i))
        if ".0"== s[-2:]:
                s=s[:-2]
        f=""
    elif f=="/":
        s=str(float(temp)/float(i))
        if ".0"== s[-2:]:
                s=s[:-2]
        f=""
    elif f=="%":
        s=str(float(temp)%float(i))
        if ".0"== s[-2:]:
                s=s[:-2]
        f=""
    if i=="*" or i=="/" or i=="%":
        temp=stack.pop()
        f=i
    else:
        stack.append(s)
        
for i in stack:
    s=i
    if f=="+":
        s=str(float(temp)+float(i))
        if ".0"== s[-2:]:
                s=s[:-2]
        f=""
    elif f=="-":
        s=str(float(temp)-float(i))
        if ".0"== s[-2:]:
                s=s[:-2]
        f=""
    if i=="+" or i=="-":
        temp=stack2.pop()
        f=i
    else:
        stack2.append(s)
if "." in stack2[0]:
    print(float(stack2[0]))
else:
    print(int(stack2[0]))