name = input("Type your name: ")
print("Welcome!", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right.Which way would you like to go?").lower()

if answer == "left":
    answer = input("You have come to a river either you can walk around or swim across.Type walk to walk around and swim to swim across: ")

    if answer == "swim":
        print("You swim across and got eaten by alligator.")
    
    elif answer == "walk":
        print("You walked many miles, ran out of water and lost.")
    
    else:
        print("Not a valid option you lose.")
    

elif answer == "right":
    answer = input("You came across a wobbly bridge, you want to cross it or head back??")

    if answer == "back":
        print("You go back to and lose")
    
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger.Do you talk to them(yes/no)?")

        if answer == "yes":
            print("The stranger showed you the way")

        elif answer == "no":
            print("You ignore the stranger.You lost the way and you lose.")

        else:
            print("Not a valid option you lose.")

    else:
        print("Not a valid option you lose.")
        

else:
    print("Not a valid option you lose.")

print("Thank you for trying",name)
