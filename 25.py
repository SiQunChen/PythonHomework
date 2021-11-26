def same_suit(card):
    for i in range(0,4):
        if card[i]+1==card[i+1] or card[i]+9==card[i+1]:
            if i==3:
                print("8")
                break
            else:
                continue
        else:
            print("5")
            break

def not_same_suit(card):
    a={}
    b=[]
    end=0
    for i in range(0,4):
        if card[i]+1==card[i+1] or card[i]+9==card[i+1]:
            if i==3:
                print("4")
                end=1
            else:
                continue
        else:
            break
    if end==0:
        for i in card:
            if not i in a:
                a[i]=1
                b.append(i)
            else:
                a[i]+=1
        k=b[-1]
        l=b[-2]
        for j in b:
            if a.get(j)==4 or a.get(k)==4:
                print("7")
                break
            elif (a.get(j)==3 and a.get(k)==2) or (a.get(k)==3 and a.get(j))==2:
                print("6")
                break
            elif a.get(j)==3 or a.get(k)==3:
                print("3")
                break
            elif (a.get(j)==2 and a.get(k)==2) or (a.get(j)==2 and a.get(l)==2) or (a.get(l)==2 and a.get(k)==2):
                print("2")
                break
            elif a.get(j)==2 or a.get(k)==2:
                print("1")
                break
            elif j==b[-1] and k==j:
                print("0")
                break

def judge(card,suit):
    card=sorted(card)
    if suit[0]==suit[1]==suit[2]==suit[3]==suit[4]:
        same_suit(card)
    else:
        not_same_suit(card)

def main():
    a={"A":14,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
    n=input().split(" ")
    card=[]
    suit=[]
    for i in n:
        if i[0]=="1":
            card.append(10)
            suit.append(i[-1])
        else:
            card.append(a[i[0]])
            suit.append(i[1])
    judge(card,suit)

main()