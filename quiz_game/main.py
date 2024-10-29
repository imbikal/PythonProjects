print("Welcome to the Quiz Game!!!")

playing = input("Hey do you want to play? ")

if playing.lower() != "yes": #.lower() changes everything to lower case for consistency
    quit()                   # So yes in whatever way (YES,yes,YeS) doesnt matter now

print("Let's go for it :) ") 
score = 0   

#Question 1
answer1 = input("What does CPU stands for? ")

if answer1 == "Central Processing Unit":
    print("That's Correct!!! Keep it up")
    score = score + 1
else:
    print("Oops!,That's incorrect")

#Question 2
answer2 = input("What does GPU stands for? ")

if answer2 == "Graphical Processing Unit":
    print("That's Correct!!! Keep it up")
    score = score + 1
else:
    print("Oops!,That's incorrect")

#Question 3
answer3 = input("What does LLM stands for? ")

if answer3 == "Large Language Model":
    print("That's Correct!!! Keep it up")
    score = score + 1
else:
    print("Oops!,That's incorrect")

#Question 4
answer4 = input("What does HDD stands for? ")

if answer4 == "Hard Disk Drive":
    print("That's Correct!!! Keep it up")
    score = score + 1
else:
    print("Oops!,That's incorrect")

#Question 5
answer5 = input("What does ML stands for? ")

if answer5 == "Machine Learning":
    print("That's Correct!!! Keep it up")
    score = score + 1
else:
    print("Oops!,That's incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%")






    