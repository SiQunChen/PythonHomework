x=str(input()).split()
meetings=[]
for i in range(int(x[1])):
    ms=str(input()).split()
    meetings.append([int(ms[1]),int(ms[2])])
meeting=sorted(meetings,key = lambda x:x[1]-x[0],reverse=True)
def counter(m):
    for li in range(len(m)):
        sum=0
        for i in range(len(m[li])):
            sum+=m[li][i]*((-1)**(i+1))
        m[li]=sum
    return m
if len(meeting)>1:
    i=0
    compare=1
    while True:
        if compare>=len(meeting):
            i+=1
            compare=i+1
        if i>=len(meeting)-1:
            break
        if meeting[i][-1]<=meeting[compare][0]:
            meeting[i]=meeting[i]+meeting[compare]
            meeting.pop(compare)
        elif meeting[i][0]>=meeting[compare][1]:
            meeting[i]=meeting[compare]+meeting[i]
            meeting.pop(compare)
        else:
            compare+=1
counter(meeting)
for i in range(int(x[0])):
    meeting.append(0)
s=0
for n in range(int(x[0])):
    s+=meeting[n]
print(s)