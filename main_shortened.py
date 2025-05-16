import random

bot = random.choice([-1,0,1])

youinput = input("Enter Your Choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[youinput]

reverse = {1:"Snake", -1:"Water", 0:"Gun"}              
print(f"You Choose {reverse[you]}\nBot Choose {reverse[bot]}")


if(bot-you==-1 or bot-you==2):
    print("YOU LOSE!")
elif(bot-you==1 or bot-you==-2):
    print("YOU WIN!")
else:
    print("IT's a DRAW")


#This logic is written on the basis of bot-you value.
