print("Number Game")
import random
playing = True 
number = str(random.randint(0,9))
print("Guess the random no. between 0 and 9 . Give your best guesses")
print("The game end when you get 1 hero right")
while playing :
    guess = int(input("Enter your best guess : "))
    if guess == number :
        print("You got it correct . You won the game !")
        print("The number is : " , number)
        break
    else:
        print("Your guess is not quite right . try again \n")