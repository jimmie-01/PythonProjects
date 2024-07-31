import random
import math

upper_limit = int(input("Enter guess upper limit: "))


if upper_limit <= 0:
    print("Enter positive integer greater than 0")
    quit()

cpu_guess = random.randint(0, upper_limit)

chances = math.ceil(math.log2(upper_limit - 0 + 1))
print(f"You have only {chances} tries to guess the number")

tries = 0

while chances:
    chances -= 1
    user_guess = int(input("Guess the number>>> "))
    tries += 1
    
    if type(user_guess) != int:
        print("Enter an integer next time!")
        continue
    
    if user_guess > cpu_guess:
        print("Try again!, you guessed too high")
    elif user_guess < cpu_guess:
        print("Try again!, you guessed to low")
    else:
        print(f"Nice!!, You got it after {tries} tries")
        quit()

print(f"Sorry!, you couldn't guess the right number, the number is {cpu_guess}")
quit()
     