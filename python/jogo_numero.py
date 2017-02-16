import random


option = int(input(''' Choose your level
		  beginner - 1
		  medium   - 2
		  hard     - 3
		  expert   - 4	
Your number goes here:'''))


if option == 1:
	rang = 10

if option == 2:
	rang = 100

if option == 3:
                rang = 1000

if option == 4:
	rang = 10000



right = random.randint(0,rang)
answer = int(input("Your bet:"))


while answer!=right:
	if answer==100000:
		print("The answer is:",right)
		break
	if answer>right:
		print("Lower!")
	else:
		print("Higher")
	answer = int(input("Your bet:"))

if answer==right:
	print("Your answer is correct")

if answer=="100000":
	print("The answer is:",right)
