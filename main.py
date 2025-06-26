import random
import csv
import matplotlib.pyplot as plt
import statistics

names = []
choices = []
choiceP1 = []
choiceP2 = []
choiceP3 = []
showlist = []
print("RULES:")
print("1. Minimum of 1 player , Maximum of 2 players (for CPU v CPU)")
print("2. Minimum of 1 player and maximum of 3 players(For multiplayer)")
print("3. Choose 2 numbers between 1 and 16 to reveal the fruit")
print("4. If you get matching fruits you receive a point")
print("5. The player with the most points when all numbers have been chosen is the winner")
print("6. NO CHEATING!!")
print()

print()
print()
print("1. Multiplayer")
print("2. CPU vs CPU")

ask = input("Choose a game mode: ")

if ask == "2":      #CPU VS CPU
  
  players = int(input("How many players are playing this game?: "))
  if players > 2:
    print("MAXIMUM OF 2 PLAYERS , PLEASE CHOOSE LESS PLAYERS")
    exit()
  if players < 1:
    print("PLEASE ENTER ATLEAST 1 PLAYER")
    exit()
  else:
    
    for i in range (players):
      name = input("What is your name?: ")
      names.append(name)
  
  ogDeck = ["APPLE","APPLE","ORANGE","ORANGE","BANANA","BANANA","GRAPE","GRAPE","PEAR","PEAR","PEACH","PEACH", "STRAWBERRY", "STRAWBERRY", "BLUEBERRY", "BLUEBERRY"]
  
  deck =     ["APPLE","APPLE","ORANGE","ORANGE","BANANA","BANANA","GRAPE","GRAPE","PEAR","PEAR","PEACH","PEACH", "STRAWBERRY", "STRAWBERRY", "BLUEBERRY", "BLUEBERRY"]
  
  numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

  
  
  random.shuffle(deck)
  

  showlist = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
  
  while len(ogDeck) != 0:
  
    
    for i in range (players):
    
        print("\n\nPlayer",i+1,"Turn")
        print(showlist)
        
        
        choice1 = random.choice(numbers) 
        choice2 = random.choice(numbers) 
        card1 = deck[choice1-1]
        card2 = deck[choice2-1]
  
        if choice1 == choice2:
          print("You have chose an incorrect match")
      
        elif card1 == card2:
          ogDeck.remove(card1)
          ogDeck.remove(card2)
          numbers.remove(choice1)
          numbers.remove(choice2)
          showlist[choice1-1] = "X"
          showlist[choice2-1] = "X"
  
          print("You have chose a correct match")
          print("You chose: ",card1)
          print("You chose: ",card2)
          
          if i == 0:
            choiceP1.append(card1)
            choiceP1.append(card2)
          elif i == 1:
            choiceP2.append(card1)
            choiceP2.append(card2)
          
  
  
        else:
          print("You have chose an incorrect match")
          print("You chose: ",card1)
          print("You chose: ",card2)
          
        if len(ogDeck) == 0:
          break
          
  print("GAME ENDED") 

  winner = ""
  numcards = 0
  
  if len(choiceP1) > len(choiceP2) :
    print(names[0] , "is the winner!!")
    winner = "player1"
    numcards = len(choiceP1)
  if len(choiceP2) >  len(choiceP1):
    print(names[1] , "is the winner!!")
    winner = "player2"
    numcards = len(choiceP2)
  if len(choiceP1) == len(choiceP2):
    print("It is a draw!!")
    winner = "draw"

  file = open("data.csv","a")
  csvWriter = csv.writer(file)

  csvWriter.writerow([winner,numcards])
  file.close()



if ask == "1":    #MULTIPLAYER
  players = int(input("How many players are playing this game?: "))
  if players > 3:
    print("MAXIMUM OF 3 PLAYERS , PLEASE CHOOSE LESS PLAYERS")
    exit()
  if players < 1:
    print("PLEASE ENTER ATLEAST 1 PLAYER")
    exit()
  else:
    
    for i in range (players):
      name = input("What is your name?: ")
      names.append(name)
  
  
  ogDeck = ["APPLE","APPLE","ORANGE","ORANGE","BANANA","BANANA","GRAPE","GRAPE","PEAR","PEAR","PEACH","PEACH", "STRAWBERRY", "STRAWBERRY", "BLUEBERRY", "BLUEBERRY"]
  
  deck = ["APPLE","APPLE","ORANGE","ORANGE","BANANA","BANANA","GRAPE","GRAPE","PEAR","PEAR","PEACH","PEACH", "STRAWBERRY", "STRAWBERRY", "BLUEBERRY", "BLUEBERRY"]
  
  
  
  
  random.shuffle(deck)
  #print(deck)      uncomment to see deck for    testing purposes
  
  showlist = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
  
  
  
  while len(ogDeck) != 0:
  
    
    for i in range (players):
    
        print("\n\nPlayer",i+1,"Turn")
        print(showlist)
       
        choice1 = int(input("Choose a number: ")) 
        choice2 = int(input("Choose a number: "))
        card1 = deck[choice1-1]
        card2 = deck[choice2-1]
  
        if choice1 == choice2:
          print("You have chose an incorrect match")
      
        elif card1 == card2:
          ogDeck.remove(card1)
          ogDeck.remove(card2)
          showlist[choice1-1] = "X"
          showlist[choice2-1] = "X"
  
          print("You have chose a correct match")
          print("You chose: ",card1)
          print("You chose: ",card2)
          
          if i == 0:
            choiceP1.append(card1)
            choiceP1.append(card2)
          elif i == 1:
            choiceP2.append(card1)
            choiceP2.append(card2)
         
            
        
      
        else:
          print("You have chose an incorrect match")
          print("You chose: ",card1)
          print("You chose: ",card2)
          
        if len(ogDeck) == 0:
          break
          
  print("GAME ENDED")      
  
  
  
  
  if len(choiceP1) > len(choiceP2):
    print(names[0] , "is the winner!!")
    winner = "player1"
    numcards = len(choiceP1)
  if len(choiceP2) > len(choiceP3) and len(choiceP2) > len(choiceP1):
    print(names[1] , "is the winner!!")
    winner = "player2"
    numcards = len(choiceP2)
  if len(choiceP1) == len(choiceP2):
    print("It is a draw!!")

  file = open("data.csv","a")
  csvWriter = csv.writer(file)

  csvWriter.writerow([winner,numcards])
  file.close()
  
  print(choiceP1)
  print(choiceP2)
  #print(choiceP3)
  print()


#open the file to read from it
file = open("data.csv","r")
fileReader = csv.reader(file)
  
winner = []
cardss = []
med = 0  
#Populate the winners list with all the winners
for row in fileReader:
  #Populate the winners list with all the winners
  winner.append(row[0])  
  cardss.append(int(row[1]))
  #med = statistics.mean(cardss)
  #print(cardss)
  
  #Calculate amount of wins
  player1Count = winner.count("player1")
  player2Count = winner.count("player2")
  drawCount = winner.count("draw")

mean = statistics.mean(cardss)
meann = round(mean,2)
print("the mean of the number of correct cards drawn by the winners is",meann)

mode = statistics.mode(cardss)
print("the mode of the numbers of correct cards drawn by the winners is",mode)

cardss.sort()
median = cardss[round((len(cardss)/2))]
print("the median of the number of correct cards drawn by the winners is",median)


#Create graph
xValues = ["P1Wins","P2Wins","Draws"]
yValues = [player1Count,player2Count,drawCount]
    
plt.bar(xValues,yValues)
plt.show()
plt.savefig("graph.png")


file.close()


   


