print("Welcome to my quiz game!")

interested = input("Do you want to play? ")

if interested.lower() != "yes":
    quit()
print("Welcome!")

score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    score += 1
    
answer = input("What does GPU stands for? ")
if answer.lower() == "graphical processing unit":
    score += 1
    
answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    score += 1
    
answer = input("What does AWS stands for? ")
if answer.lower() == "amazon web services":
    score += 1
    
average = (score / 4) * 100

if average < 50:
    print(f"You score is {average}% and it is below average")
else:
    print(f"Your score is {average}%, you passed the quiz!")
    