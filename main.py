from random import randint

yes = 1
no = 2
play = 1

while play == yes:
  value = (randint(0,9)) 
  print value
  print("what is the random number")
  user_input = int(input())
  while user_input != value:
    print("sorry try again" ,str(user_input))
    user_input = int(input())
  if user_input == value:
    print "congrats"
    print "Do you want to play again, type 1 for Yes or 2 for No?"
  
  new_input = int(input())
  if new_input != yes:
    print"game has ended."
    play = 2
  else:   
    print "play again"