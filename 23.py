def computer_only(number,player_number,computer_number):
    for i in range(30):
        if computer_number>10.5:
            computer_number=0
            break
        else:
            if computer_number<player_number or computer_number<=8:
                computer_number=computer_number+computer_Y(number)
            else:
                break
    return computer_number

def player_only(number,player_number):
    for i in range(30):
        if player_number>10.5:
            player_number=0
            break
        else:
            player_choose=str(input())
            if player_choose=="Y":
                player_number=player_number+player_Y(number)
            else:
                break
    return player_number

def computer_Y(number):
    computer_number=str(input())
    computer_number=number[computer_number]
    return computer_number

def player_Y(number):
    player_number=str(input())
    player_number=number[player_number]
    return player_number

def main():
    number={"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":0.5,"Q":0.5,"K":0.5}
    player_number=str(input())
    player_number=number[player_number]
    computer_number=str(input())
    computer_number=number[computer_number]
    for i in range(30):
        if computer_number>10.5:
            computer_number=0
            break
        elif player_number>10.5:
            player_number=0
            break
        player_choose=str(input())
        if player_choose=="Y":
            player_number=player_number+player_Y(number)
        else:
            computer_number=computer_only(number,player_number,computer_number)
            break
        if computer_number<player_number or computer_number<=8:
            computer_number=computer_number+computer_Y(number)
        else:
            player_number=player_only(number,player_number)
            break
    print(f"{float(player_number)} vs. {float(computer_number)}")
    if player_number > computer_number:
        print("player wins")
    elif player_number < computer_number:
        print("computer wins")
    else:
        print("It's a tie")

main()