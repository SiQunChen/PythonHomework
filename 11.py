course={}
ans=[]
for i in range(3):
    course_num=input()
    hours=int(input())
    for j in range(hours):
        temp=input()
        if course.get(temp)==None:
            course[temp]=course_num
        else:
            ans.append(f"{course.get(temp)} and {course_num} conflict on {temp}")
for i in ans:
    print(i)
