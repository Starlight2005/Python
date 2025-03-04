# Bumper Cars

height = int(input('What is your height (cm)? '))
age = int(input('What is your age? '))
credits = int(input('How many credits do you have? '))

if height >= 120 and age >= 8 and credits >= 5:
  print("Enjoy the Bumper Cars!")
elif height < 120 and age >= 8 and credits >= 5:
  print("You are not tall enough to ride.")
elif age < 8 and height >= 120 and credits >= 5:
  print("You are not old enough to ride.")
elif credits < 5 and height >= 120 and age >= 8:
  print("You don't have enough credits.")
else:
  print("You do not meet the requirements to ride the Bumper Cars.")
