import random
user_wins=0
comp_wins=0
options=["rock","paper","scissors"]
while True:
    user_input=input("Type Rock/Paper/Scissors  to  play  or  Q  to quit the game :- ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
    else:
        random_number=random.randrange(0,3)
        # for rock = 0 , for paper = 1 ,for scissors = 2
        computer_pick=options[random_number]
        print("Computer Picked :- ",computer_pick)
        if user_input==computer_pick:
            print("Game Tied")
        elif user_input=="rock" and computer_pick=="paper":
            print("Computer wins..")
            comp_wins+=1
        elif user_input=="rock" and computer_pick=="scissors":
            print("You  Wins ...")
            user_wins+=1
        elif user_input=="paper" and computer_pick=="rock":
            print("You win ..")
            user_wins+=1
        elif user_input=="paper" and computer_pick=="scissors":
            print("Computer wins...")
            comp_wins+=1
        elif user_input=="scissors" and computer_pick=="paper":
            print("You win...")
            user_wins+=1
        else:
            print("Computer wins..")
            comp_wins+=1
print("You won ",user_wins,"times")
print("Computer  won ",comp_wins,"times")
print("Goodbye!!!")