# Fortune Cookie Generator 

import random

enter = input('Enter to open your fortune cookie...')

random_number = random.randint(1, 10)

if random_number == 1:
  answer = 'You will have a great day today!'
elif random_number == 2:
  answer = 'A surprise is waiting for you.'
elif random_number == 3:
  answer = 'Luck is on your side!'
elif random_number == 4:
  answer = 'Be cautious of new opportunities.'
elif random_number == 5:
  answer = 'Your hard work will soon pay off.'
elif random_number == 6:
  answer = 'Someone is thinking about you right now.'
elif random_number == 7:
  answer = 'A big change is coming your way.'
elif random_number == 8:
  answer = 'You will make a new friend soon.'
elif random_number == 9:
  answer = 'Success is just around the corner!'
elif random_number == 10:
  answer = 'Happiness comes to those who wait.'
else:
  answer = 'Error: No fortune found!'

print('Your fortune: '+answer)
