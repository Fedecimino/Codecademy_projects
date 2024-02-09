#importing random we will have an answer different each time

import random
# assing the name of the playeer
name='federica'
#variable asking user yes or not
question='yes or not'
# this variable is an open string and will store the answers

answer= " "


# this variable will store the random generated numbers

random_number= random.randint(1,9)

print (random_number)

# now we implement our game with the logic of our program

if random_number == 1:
  print("Yes - definitely")

elif random_number == 2:
  print("is decidedly so")
elif random_number == 3:
  print("Without a doubt")
elif random_number == 4:
  print("Reply hazy, try again")
elif random_number == 5:
  print("Ask again later")
elif random_number == 6:
  print("Better not tell you now")
elif random_number == 7:
  print("My sources say no")
elif random_number == 8:
  print("Outlook not so good")
elif random_number == 9:
  print("Very doubtful")
else:
  print("error")

print(name + " asks: " + question)

print("Magic 8 Ball's answer: " + answer)
