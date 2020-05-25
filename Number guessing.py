import random
jackpot=random.randint(1, 100)
guess=int(input("Guess one integer number between 1-100 and you have 10 chances\U0001F603:"))
counter=1
while jackpot != guess:
    counter+=1
    x=10-counter
    if counter>10:
        print("No chances left!!\U0001F62A")
    if guess>jackpot:
        print(x,"Chances are left!!")
        guess=int(input("Guess lower\U0001F914:"))
    else:
        print(x, "chances are left!!")
        guess=int(input("Guess higher\U0001F914:"))
else:
    print("Your guess is right!!\U0001f601")
    print("You took",counter,"attempts to guess the right one!!\U0001f917")
