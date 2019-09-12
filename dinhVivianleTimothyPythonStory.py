"""
Apythonlypse
Authors: Vivian Dinh, Timothy Le
Date: 9/11/19
"""
import time
import sys

#Introduction to Story
def exposition():
  sys.stdout.write("\033[1;30;40m")
  intro ="""
  You sit in your car admist heavy traffic... 
  On the news, you hear reports of the government being overthrown... 
  All hell breaks loose and you are stuck in your car while 
  People run on the street in pure chaos...
  Should you leave your car and run, or stay?
  """
  sys.stdout.write("\033[1;m")
  for l in intro:
   sys.stdout.write(l)
   sys.stdout.flush()
   time.sleep(0.1)
  sys.stdout.write("\033[1;34;40m")
  car =str(input("Run or Stay: "))
  sys.stdout.write("\033[1;m")
  car = car.lower()
  if(car in run):
    leave()
    return()
  elif(car == "stay"):
    sit()
    return()
  else:
    print("""
    Please choose an option
    """)
    return exposition()
#this is the choice to stay in the car after chaos breaks loose.   
def sit():
  hotCar ="""
  After staying in the car for hours, you decide to leave
  Do you look for food first or get help first?
  """
  for l in hotCar:
   sys.stdout.write(l)
   sys.stdout.flush()
   time.sleep(0.1)
#this is the situation where the text is supposed to turn into different colors
  food =str(input("\033[1;34;40m"+"Food"+"\033[1;m"+" or "+"\033[1;34;40m"+"Help"+"\033[1;m"+": "))
  food = food.lower()
  if(food == "food"):
    print("""
    You go get food
    """)
    leave()
  elif(food == "help"):
    leave()
  else:
    print("""
    Please choose an option
    """)
    sit()
  #other choice to leave car 
def leave():
  streetFighter = """
  Now that you've left, you've met up with others and you run together
  Oh no!
  The police are blocking the roadway
  You can't get off the road!!!!
  Should you fight them or comply?
  """
  for l in streetFighter:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.1)
  police = str(input("\033[1;34;40m"+"Fight"+"\033[1;m"+" or "+"\033[1;34;40m"+"Comply"+"\033[1;m"+": "))
  police = police.lower()
  if(police == "fight"):
    punch()
  elif(police == "comply"):
    comply()
  else:
    print("Please choose an option")
    leave()
#option to comply with the police 
def comply():
  take = """
  The police take you to a containment camp
  You find out that the containment camp is dangerous to stay at
  Should you stay at the camp or leave by fighting the police?
  """
  for l in take:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.1)
  police=str(input("\033[1;34;40m"+"Stay"+"\033[1;m"+" or "+"\033[1;34;40m"+"Leave"+"\033[1;m"+": "))
  police = police.lower()
  #Option to stay at camp
  if(police=="stay"):
   stay ="""
   The camp limited the amount of resources and you die of bubonic plague
   \033[1;31;40m Game Over \033[1;m
   """
   for l in stay:
      sys.stdout.write(l)
      sys.stdout.flush()
      time.sleep(0.1)
   playAgain()
   return()
  #Option to leave camp
  elif(police == "leave"):
    dysentary = """
    You win the fight!
    But you contract an infection and die of dysentary
    \033[1;31;40m Game Over :( \033[1;m
    """
    for l in dysentary:
      sys.stdout.write(l)
      sys.stdout.flush()
      time.sleep(0.1)
  else:
    print("""
    Please choose an option
    """)
    return comply()
    playAgain()
    return()

#When you fight the police
def punch():
  winner ="""
  You won the fight, hooray!
  But half your group dies in the battle
  Luckily, you find shelter in a school with food and supplies
  However, there's only food for half of the group
  Will you take the food or be kind and give to others?
  """
  for l in winner:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.1)
  give = str(input("\033[1;34;40m"+"Take"+"\033[1;m"+" or "+"\033[1;34;40m"+"Give"+"\033[1;m"+": "))
  give = give.lower()
  #Option to take food
  if(give == "take"):
    survive()
  #Option to give food
  elif(give == "give"):
    groupDie()
  else:
    print("Please choose an option")
    punch()
#Outcome of giving food
def groupDie():
  starvation = """
  You die of starvation
  \033[1;31;40m + Game Over :( + \033[1;m
  """
  for l in starvation:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.1)
  playAgain()
  return()
#Outcome of taking food
def survive():
  live = """
  Half of the group dies, but you live
  After traveling for several days, you find a safe haven
  \033[1;32;40m You win! \033[1;m
  """
  for l in live:
      sys.stdout.write(l)
      sys.stdout.flush()
      time.sleep(0.1)
  playAgain()
  return()
#Play again loop
def playAgain():
  play = str(input("\033[1;35;40m"+"Play Again?"+"\033[1;m"+": "))
  play = play.lower()
  if(play in ans):
    exposition()
  else:
    print("Goodbye")
    return()
ans = "yes","ye","yeah","yos"
run = "run","leave","leave car"
exposition()
