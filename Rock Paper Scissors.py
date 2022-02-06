import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

map =[rock, paper, scissors]
print("\t\t\t\t\t\tWelcome to ROCK PAPER SCISSORS!!!\nHow to Play?\nA rock beats scissors, scissors beat paper by cutting it, and paper beats rock by covering it.")
print("NOTE: Hit 1 for Rock, 2 for Paper & 3 for Scissors")
usrInp = int(input())
print(map[usrInp-1])
comChoice = random.randint(0,2)
print(map[comChoice]) 
if usrInp-1 == comChoice:
    result = "DRAW!!! No One Wins!"
elif (usrInp == 1 and comChoice == 2) or (usrInp == 2 and comChoice == 0) or (usrInp == 3 and comChoice == 1):
  result = "User Wins!!!\nCongrats!!!!"
else:
  result = "Computer Wins!!!\nTry Again Baby!"
print(result)