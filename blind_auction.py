from replit import clear
from art import logo
print (logo)
#name = input("What is your name?\n")
#bid = input("What is your bid?\n")
#print (f"My name is {name} and my bid is {bid}")
auction = []
def add_auction(username, bid_amount):
  new_auction= {}
  new_auction["name"] = username
  new_auction["bid"] = bid_amount
  auction.append (new_auction)
def find_max(auction_list):
  max = 0
  for element in range(0,len(auction)):
    if auction[element]["bid"] > max:
      max = auction[element]["bid"]
      winner = auction[element]["name"]
  print(f"Maximum amount of {max} has been proposed by {winner}")

continuation = True
while continuation:
  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n"))
  print (f"My name is {name} and my bid is {bid}")
  add_auction(name,bid)
  should_continue = input("Are there any other people to continue? Write 'yes' or 'no'\n")
  if should_continue == "yes":
    continuation = True
    clear()
  else:
    continuation = False
find_max (auction)
#HINT: You can call clear() to clear the output in the console.
