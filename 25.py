def main():
    a={"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":0.5,"Q":0.5,"K":0.5}
    n=str(input())
    number=''.join([x for x in n if x.isdigit()])
    print(n)

main()