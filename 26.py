def main():
    #points跟scores寫反了，以下points為贏或輸的分數，scores為手牌點數。
    bank=0
    two_times_perfect=[]
    five_card=[]
    points=[]
    number={"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":0.5,"Q":0.5,"K":0.5}
    people=int(input())
    bet=input().split(" ")
    scores=input().split(" ")
    for i in range(people):
        scores[i]=number[scores[i]]
        bet[i]=int(bet[i])
        points.append(0)
        two_times_perfect.append(i)
        five_card.append(i)
        for j in range(4):
            choose=input()
            if choose == "Y":
                scores[i]=number[input()]+int(scores[i])
                if scores[i]>10.5:
                    points[i]=0-bet[i]
                    bank+=bet[i]
                    break
                elif j==3 and scores[i]<10.5:
                    points[i]=0+bet[i]
                    bank-=bet[i]
                    five_card=100
                    break
                elif scores[i]==10.5 and j==0:
                    points[i]=0+bet[i]
                    bank-=bet[i]
                    two_times_perfect[i]=100
                    break
            elif choose == "N":
                break
    bank_scores=number[input()]
    for i in range(4):
        choose=input()
        if choose=="Y":
            bank_scores=number[input()]+bank_scores
            if bank_scores>10.5:
                for i in range(people):
                    if scores[i]<=10.5:
                        points[i]+=bet[i]
                        bank-=bet[i]
                break
        elif choose=="N":
            break
    if bank_scores<=10.5:
        for i in range(people):
            if (scores[i]<10.5 and five_card!=100) or (two_times_perfect[i]!=100 and scores[i]==10.5):
                if bank_scores>=scores[i]:
                    points[i]-=bet[i]
                    bank+=bet[i]
                else:
                    points[i]+=bet[i]
                    bank-=bet[i]
    for i in range(people):
        name="Player"+str(i+1)
        if points[i]>0:
            print(f"{name} +{points[i]}")
        else:
            print(f"{name} {points[i]}")
    if bank>0:
        print(f"Bank +{bank}")
    else:
        print(f"Bank {bank}")
main()