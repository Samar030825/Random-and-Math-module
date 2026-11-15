import random
while True :
    user_action = input("Enter a choice ( Rock , Paper , Scissor)")
    possible_action = ["rock" , "paper" , "scissor"]
    computer_action = random.choice(possible_action)
    print(f"You choosed {user_action} and computer choosed {computer_action}")

    if computer_action == user_action :
        print(f"Both player choosed {user_action}. It is a tie !")

    elif user_action == "rock":
        if computer_action == "scissor":
            print("Rocks smashes scissor . You won")
        else :
            print("paper cover rock . You lose !")

    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper cover rock . You win !")
        else:
            print("Scissor cut paper . You lose !")

    elif user_action == "scissor":
        if computer_action == "paper":
            print("Scissor cut paper . you win!")
        else:
            print("Rock smashes scissor. You lose!")

    play_again = input("Play again(y/n) :")
    if play_again != "y":
        break