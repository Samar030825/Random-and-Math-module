import random
import math

lucky_number = random.randint(1,100)
print("Your lucky no. is : " , lucky_number)

fun_activity = [ "Play hand cricket " , "Start drawing" , "Study" , "Do your chores " , "Play outdoor "]
random_activity = random.choice(fun_activity)
print("your fun activity is : " , random_activity)

secret_number = random.randint(1,20)
print("Guess the random no. between 1 and 20")
while True:
    guess = int(input("Enter your guess :"))
    if guess == secret_number:
        print("Correct you won the game")
        break
    else :
        print("Wrong ! Try again !")

decimal_number = float(input("Enter a decimal no."))

print("Cieling answer : " , math.ceil(decimal_number))
print("Floor anser : " , math.floor(decimal_number))

x = -5
y = 10

print("Copy sign result : " , math.copysign(x ,y))

neg_number = int(input("Enter a negative number : "))
print("absolute value : "  , math.fabs(neg_number))

num_1 = int(input("Enter the first no."))
num_2 = int(input("Enter the second no."))

print("Their gcd is : " , math.gcd(num_1, num_2))
