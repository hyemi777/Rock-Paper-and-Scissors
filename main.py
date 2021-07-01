import random

while True: 
  choices = ['rock', 'paper', 'scissors']
  computerChoice = choices[random.randint(0,2)]

  userChoice = input("What is your choice? (Rock, paper, scissors)\n")
  if userChoice == computerChoice :
    print("Tie! Try again.")
    
  elif (userChoice == "rock" and computerChoice == "paper") or (userChoice == "scissors" and computerChoice == "rock") or (userChoice == "paper" and computerChoice == "scissors"):
    print("Computer wins!")

  elif (userChoice == "rock" and computerChoice == "scissors") or (userChoice == "scissors" and computerChoice == "paper") or (userChoice == "paper" and computerChoice == "rock"):
    print("You win!")
  else :
    print("I can't do that yet.")
