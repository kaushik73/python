# text = input("Enter the text you wants to reverse")
# text_rev= text[::-1]

# print (text_rev)

# def sum (a,b):
#     s = a+b
#     # print (s)
#     return s


# print("HII")
# sums=sum(5,5) 
# print(sums)
# sum(3,2)
# sd=sum(3,3)

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


#harry tut.24
# print("Enter num 1")
# num1 = input()
# print("Enter num 2")
# num2 = input()
# try:
#     print(f"The sum of these two numbers is" )
#     print(int(num1 + num2))


# except Exception as e :
#     print(e)

# print("This line is very important")


#harry tut.26
# f = open("python50.py")
# con = f.read(2)
# print("1",con)
# f.close()


# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

#harry tut.27    The number guessing game .
# no of guesses 9
#  print no of guesses left
# No of guesses he took to finish
# game over
# n=18
# number_of_guesses=1
# print("Number of guesses is limited to only 9 times: ")
# while (number_of_guesses<=9):
#     guess_number = int(input("Guess the number :\n"))
#     if guess_number<18:
#         print("you enter less number please input greater number.\n")
#     elif guess_number>18:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(number_of_guesses,"no.of guesses he took to finish.")
#         break
#     print(9-number_of_guesses,"no. of guesses left")
#     number_of_guesses = number_of_guesses + 1

# if(number_of_guesses>9):
#     print("Game Over")

# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------


#lecture 29     solution STAR GAME 
# a = int(input("please add number of line you want to print\n"))
# b = bool(int(input("please ENTER 0 for False \t 1 for True \n")))
# # if entered number is other than 0 or 1 then also system takes it as true.

# def star(a, b):
#     if b == True:
#         c = 1
#         while c <= a:
#             print(c * "*")
#             c = c + 1
#     if b== False :
#         while a > 0:
#             print(a * "*")
#             a = a - 1
#     return "End"        
# star(a,b)
# print(star(0,0))

##### print statement k andar agar fuction ko call karenge too vo uske return ko print karega 
##### aaur agar normally direct function likh denge kuch iss tarah #star(a,b)#
##### too vo jo function aandar print kar raha hai vo karega.


# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------

# Health Management System
# Total 6 Files, 3 For exercise and 3 For for diet
# 3 clients - Harry, Rohan and Hammad
# write a function that when executed takes as input client name
# one more function to retrieve exercise or food for any client

# import datetime

# def getdate():
#     return datetime.datetime.now()

# def add_func(client):
#     if client == "1":
#         exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
#         add_item = input("What do you want to Add? : ")
#         if exer_diet == "1":
#             with open("harry_exer.txt","a") as f:
#                 add = [" [",getdate(),"] ",add_item,"\n"]
#                 for item in add:
#                     f.write("%s" % item) 
#             print("Item successfully added")        
#         elif exer_diet == "2":
#             with open("harry_diet.txt","a") as f:
#                 add = [" [",getdate(),"] ",add_item,"\n"]
#                 for item in add:
#                     f.write("%s" % item) 
#             print("Item successfully added")          
#     elif client == "2":
#         exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
#         add_item = input("What do you want to Add? : ")
#         if exer_diet == "1":
#             with open("rohan_exer.txt","a") as f:
#                 add = [" [",getdate(),"] ",add_item,"\n"]
#                 for item in add:
#                     f.write("%s" % item) 
#             print("Item successfully added")        
#         elif exer_diet == "2":
#             with open("rohan_diet.txt","a") as f:
#                 add = [" [",getdate(),"] ",add_item,"\n"]
#                 for item in add:
#                     f.write("%s" % item) 
#             print("Item successfully added")         
#     elif client == "3":
#         exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
#         add_item = input("What do you want to Add? : ")
#         if exer_diet == "1":
#             with open("hammad_exer.txt","a") as f:
#                 add = [" [",getdate(),"] ",add_item,"\n"]
#                 for item in add:
#                     f.write("%s" % item) 
#             print("Item successfully added")        
#         elif exer_diet == "2":
#             with open("hammad_diet.txt","a") as f:
#                 add = [" [",getdate(),"] ",add_item,"\n"]
#                 for item in add:
#                     f.write("%s" % item) 
#             print("Item successfully added") 
# def retrive_func(client):
#     if client == "1":
#         exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
#         if exer_diet == "1":
#             try:
#                 with open("harry_exer.txt","r") as f:
#                     print("\nFile items\n")
#                     for i in (f.readlines()):
#                         print(i)
#             except:
#                 print("Items does not retrieve. Please add some items in file")        
#         elif exer_diet == "2":
#             try:
#                 with open("harry_diet.txt","r") as f:
#                     print("\nFile items\n")
#                     for i in (f.readlines()):
#                         print(i) 
#             except:
#                 print("Items does not retrieve. Please add some items in file")                
#     elif client == "2":
#         exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
#         if exer_diet == "1":
#             try:
#                 with open("rohan_exer.txt","r") as f:
#                     print("\nFile items\n")
#                     for i in (f.readlines()):
#                         print(i)
#             except:
#                 print("Items does not retrieve. Please add some items in file")         
#         elif exer_diet == "2":
#             try:
#                 with open("rohan_diet.txt","r") as f:
#                     print("\nFile items\n")
#                     for i in (f.readlines()):
#                         print(i)
#             except:
#                 print("Items does not retrieve. Please add some items in file")         
#     elif client == "3":
#         exer_diet = input("Enter number 1 for exercise or 2 for diet : ")
#         if exer_diet == "1":
#             try:
#                 with open("hammad_exer.txt","r") as f:
#                     print("\nFile items\n")
#                     for i in (f.readlines()):
#                         print(i)
#             except:
#                 print("Items does not retrieve. Please add some items in file")         
#         elif exer_diet == "2":
#             try:
#                 with open("hammad_diet.txt","r") as f:
#                     print("\nFile items\n")
#                     for i in (f.readlines()):
#                         print(i)
#             except:
#                 print("Items does not retrieve. Please add some items in file")          

# client = input("Enter number 1 for harry, 2 for rohan and 3 for hammad : ") 
# add_retrieve = input("Enter number 1 for Add and 2 for Retrieve : ")

# if add_retrieve == "1":
#     add_func(client)
# elif add_retrieve == "2":
#     retrive_func(client)

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------


# Snake water gun

import random
lst = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

# making the game in while
while no_of_chance < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n ")

    # if user enter s
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter g

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point==human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")

#
# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
# Stone = Snake
# Scissor = Water
# Paper = Gun


  




  
