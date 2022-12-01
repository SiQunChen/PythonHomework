def main():
    special=input()
    spe=input()
    head=input().split()
    six=input().split()
    pen=int(input())
    number=[input() for i in range(pen)]
    money=0
    for i in number:
        if i == special:
            money+=10000000
        elif i == spe:
            money+=2000000
        elif i==head[0] or i==head[1] or i==head[2]:
            money+=200000
        elif i[1:]==head[0][1:] or i[1:]==head[1][1:] or i[1:]==head[2][1:]:
            money+=40000
        elif i[2:]==head[0][2:] or i[2:]==head[1][2:] or i[2:]==head[2][2:]:
            money+=10000
        elif i[3:]==head[0][3:] or i[3:]==head[1][3:] or i[3:]==head[2][3:]:
            money+=4000
        elif i[4:]==head[0][4:] or i[4:]==head[1][4:] or i[4:]==head[2][4:]:
            money+=1000
        elif i[5:]==head[0][5:] or i[5:]==head[1][5:] or i[5:]==head[2][5:]:
            money+=200
        elif i[5:]==six[0] or i[5:]==six[1] or i[5:]==six[2]:
            money+=200
        else:
            pass
    if money == 0:
        print("0")
    else:
        print(money)

main()