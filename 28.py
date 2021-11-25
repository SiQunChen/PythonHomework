def main():
    n=input().split()
    for i in range(len(n)):
        n[i]=int(n[i])
    for i in range(1000000):
        if i%n[0]==n[1] and i%n[2]==n[3] and i%n[4]==n[5]:
            print(i)
            break

main()