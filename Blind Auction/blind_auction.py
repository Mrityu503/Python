import art
from replit import clear
#HINT: You can call clear() to clear the output in the console.
print("Welcome to secret auction program!")
print(art.logo)
go_again = "yes"
auction = {}
while go_again == "yes":
  name = input("What is your name?: ")
  bid = input("What's your bid?: $")
  auction[name] = bid
  go_again = input("Are there any other bidders? Type 'yes' or 'no'.")  
  clear()
winner = max(auction, key = auction.get)
print(f"The winner is {winner} with a bid of ${auction[winner]} ")

#Alternate for clear other than replit
# from os import system
# system("clear")
# It may not work on pycharm.
