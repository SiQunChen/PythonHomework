p = 10 ** 9 + 7
a = [[0] * 10 for i in range(10 ** 5 + 1)]

for i in range(1, 10 ** 5 + 1):
    for j in range(9, 0, -1):
        if i == 1 or j == 9:
            a[i][j] = 1
        else:
            a[i][j] = (a[i][j + 1] + a[i - 1][j]) % p

data = [input()]
for N in data:
    l, ans, isladder = len(N), 0, 1
    for i in range(1, l):
        if N[i] < N[i - 1]:
            isladder = 0
            break
    ans += isladder #判斷自己是不是階梯數字

    for i in range(1, l):
        for j in range(1, 10):
            ans += a[i][j] #將自身位數-1的所有階梯數字加起來，例如1024:將1~999的階梯數字全部相加

    for j in range(1, int(N[0])):
        ans += a[l][j] #將自身位數、開頭為N[0]-1~1的數字全部相加，例如896:將三位數並且開頭為7~1的階梯數字相加

    for i in range(1, l):
        if N[i] >= N[i - 1]:
            for j in range(int(N[i - 1]), int(N[i])):
                ans += a[l - i][j] #逐位檢察，如果相鄰的兩個數字為階梯函數，將範圍內的所有階梯數字相加
        else:     #例如3572:35為階梯數字，將3333~3499的階梯數字相加(程式將位數-1，做3位數並且開頭為3~4的所有階梯數字)
            break #57為階梯數字，將3555~3569的階梯數字相加(同上)
    print(ans,end="") #72不為階梯數字，後面不可能出現階梯數字，所以跳出迴圈