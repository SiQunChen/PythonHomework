name=str(input())
birthday=str(input())
a=name.find(" ")
f=name[:a]
l1=name[a:]
l2=l1[1:]
y=birthday[0:4:1]
m=birthday[5:7:1]
d=birthday[8:10:1]
str="{FirstName} is born at year {yyyy} month {mm} day {dd} in {LastName} family.".format(FirstName=f,yyyy=y,mm=m,dd=d,LastName=l2)
print(str)