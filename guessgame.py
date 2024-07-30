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
    user_guess = int(input("Guess the number>>> "))
    if type(user_guess) != int:
        print("Enter an integer next time!")
        continue
    
    if user_guess > cpu_guess:
        print("Try again!, you guessed too high")
        chances -= 1
        tries += 1
    elif user_guess < cpu_guess:
        print("Try again!, you guessed to low")
        chances -= 1
        tries += 1
    else:
        tries += 1
        print(f"Nice!!, You got it after {tries} tries")
        quit()

print("Sorry!, you couldn't guess the right number")
quit()
     