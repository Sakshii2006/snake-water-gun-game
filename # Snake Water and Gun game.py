# Snake Water and Gun game
'''
-1 for snake
1 for water
0 for gun
'''
import random

computer = random.choice([-1, 1, 0])
 
you= input("Enter your choice: 's' for snake, 'w' for water or 'g' for gun\n")
youDict = { "s": -1, "w": 1, "g": 0}
reverseDict = { -1: "snake", 1:"water", 0:"gun"}

you= youDict[you]
print(f"\nyou choose {reverseDict[you]} \n compputer choose {reverseDict[computer]}")

if computer == you:
 print("It's draw")

elif (computer == 1 and you == -1) or (computer == 0 and you == 1) or (computer == -1 and you == 0):
   print ("you win!")
   
else : 
   print("computer win")

