def transferPoint(card):
    pork = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    points =[1,2,3,4,5,6,7,8,9,10,0.5, 0.5,0.5]
    index = pork.index(card) 
    return points[index]

def getSum(x,y,z):
    pointSum = transferPoint(x)+transferPoint(y)+transferPoint(z)
    if pointSum>10.5:
        pointSum=0
    return pointSum

def compare(A,B):
    print(A)
    print(B)
    if A>B:
        print("A Win")
    elif A<B:
        print("B Win")
    else:
        print("Tie")
        
def main():
    x1=input()
    x2=input()
    x3=input()
    y1=input()
    y2=input()
    y3=input()
    A=getSum(x1,x2,x3)
    B=getSum(y1,y2,y3)
    compare(A, B)

main()

    
    