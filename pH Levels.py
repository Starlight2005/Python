# pH Levels

ph = int(input('Enter a pH level between 0 and 14: '))

if ph > 7:
  print('Basic')
elif ph < 7:
  print('Acidic')
else:
  print('Neutral')
