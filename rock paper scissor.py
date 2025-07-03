import random
print("Welcome to Rock , Paper , Scissors!")
computer=random.choice(['Rock','Paper','Scissor'])
you=input("enter your choice : ")
while you not in ['Rock','Paper','Scissors']:
    print("invalid input. Please try again")
    you=input("enter yur choice : ")
print(f"You chose : {you}")
print(f"Computer chose : {computer}")
if (computer==you):
    print("Draw")
elif (computer=='Rock' and you=='Paper'):
    print("You Won!")
elif (computer=='Paper' and you=='Scissor'):
    print("You Won!")
elif (computer=='Scissor' and you=='Rock'):
    print("You Won!")
else:
    print("Computer Wins!")