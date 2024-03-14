import random

# Select a random item

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
gamer = []

def deal_card(cards):
  selected_item = random.choice(cards)
  return selected_item



def game():
  gamer.append(deal_card(cards))
  return gamer

def sum_score(gamer_result):
  sum = 0
  for i in range(0,len(gamer_result)):
    sum += gamer[i]
  return sum

user_card = []
computer_card = []

while sum_score (user_card) < 17:
  user_card = game()
  print(user_card)
  print(sum_score(user_card))
