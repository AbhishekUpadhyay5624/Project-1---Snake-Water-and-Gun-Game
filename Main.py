#'Snake' , 'Water' and 'Gun' Game 
'''
1 for snake
-1 for water
0 for gun
'''
import random

bot = random.choice([-1,0,1])

youinput = input("Enter Your Choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[youinput]

reverse = {1:"Snake", -1:"Water", 0:"Gun"}              
print(f"You Chose {reverse[you]}\nBot Chose {reverse[bot]}")

if(bot == -1 and you == 1):
    print("YOU WIN! ")
elif(bot == -1 and you == 0):
    print("YOU LOSE! ")
elif(bot == 1 and you == -1):
    print("YOU LOSE! ")
elif(bot == 1 and you == 0):
    print("YOU WIN! ")
elif(bot == 0 and you == -1):
    print("YOU WIN! ")
elif(bot == 0 and you == 1):
    print("YOU LOSE! ")
elif(bot == you):
    print("DRAW!")
else:
    print("Something went wrong")

