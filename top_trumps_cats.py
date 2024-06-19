import random
import requests
import time
import json
api_key = 'L7UBeFru1js/XajzwSwe7g==JMga4cLaUQOQZP6a'

# Color constants
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
reset = "\033[0m"

# Function to get all cats
def get_all_cats():
    all_cat_list = []
    for number in range(1, 5):
        api_url = 'https://api.api-ninjas.com/v1/cats?family_friendly={}'.format(number)
        response = requests.get(api_url, headers={'X-Api-Key': api_key})
        all_cats = response.json()
        for cat in all_cats:
            if cat["name"] not in all_cat_list:
                all_cat_list.append(cat["name"])
    return all_cat_list

# Function to get cat stats
def get_cat_stats(cat_name):
    api_url = 'https://api.api-ninjas.com/v1/cats?name={}'.format(cat_name)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    cat_data = response.json()
    return cat_data

def cat_scoreboard(players):
    scoreboard = {"You": 0}
    for i in range(1, players + 1):
        scoreboard[f"Computer {i}"] = 0
    return scoreboard

def display_scoreboard(scoreboard):
    print("\nSCOREBOARD:")
    for player, score in scoreboard.items():
        print(f"{player}: {score} points")


def start_game():

  # Variables
  valid_cat_list = get_all_cats()
  random_cats = random.sample(valid_cat_list, 4)
  my_cat = random_cats[0]
  opponent_cats = random_cats[1:]
  available_stats = [
      'playfulness',
      'shedding',
      'family_friendly',
      'other_pets_friendly',
  ]

  # Get stats for each cat
  my_stat = get_cat_stats(my_cat)[0]
  opponent_stats = [get_cat_stats(cat)[0] for cat in opponent_cats]

  # Execution
  print("Welcome to Top Trumps!")
  cat_ascii_art = r"""
   /\_/\
  ( o.o )
   > ^ <
  """
  print(cat_ascii_art)
  print()
  players = 0
  while players >4 or players <=0:
      players = int(input('How many players would you like to play against (1-3)? '))
  time.sleep(1)
  print()
  print(f'You were given {my_cat}')
  time.sleep(1)
  for i in range(players):
      print(f'{blue}Computer {i+1} was given {yellow}{opponent_cats[i]}{reset}')
  time.sleep(1)
  scoreboard = cat_scoreboard(players)
  print()
  print("Available stats:\n")
  for i, stat in enumerate(available_stats, 1):
      print(f"{i}. {stat} ({my_stat[stat]})")
  stat_choice = int(input("Please select a category to battle (1-4): "))
  print()
  if stat_choice >= 1 and stat_choice <= 4:
      selected_stat = available_stats[stat_choice - 1]
      print(f"You selected category: {green}{selected_stat}{reset}")
  else:
      print(f"{red}Invalid category selection.{reset}")
      exit()
  time.sleep(2)
  print("\nThe battle begins!\n")
  time.sleep(1)
  print(f"Your card: {my_cat} | {selected_stat} | {my_stat[selected_stat]}")
  time.sleep(1)
  for i in range(players):
      print(f"{blue}Computer {i+1} card{reset}: {opponent_cats[i]} | {selected_stat} | {opponent_stats[i][selected_stat]}")
  time.sleep(2)
  print()
  for i in range(players):
      if my_stat[selected_stat] > opponent_stats[i][selected_stat]:
          print(f'{magenta}Congratulations, you have Trumped computer {i+1}!{reset}')
          scoreboard["You"] += 1

      elif my_stat[selected_stat] < opponent_stats[i][selected_stat]:
          print(f'{red}Tough luck, computer {i+1} has Trumped you!{reset}')
          scoreboard[f"Computer {i+1}"] += 1
      else:
          print(f'{cyan}Draw with computer {i+1}!{reset}')
  print()
  display_scoreboard(scoreboard)

while True:
    start_game()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        print('NEXT ROUND STARTS')
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break