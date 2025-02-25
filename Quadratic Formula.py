# Quadratic Formula 

a = int(input('Enter a: ')) # Take as 2 for example
b = int(input('Enter b: ')) # Take as -5 for example
c = int(input('Enter c: ')) # Take as -3 for example 

x1 = (-b + (b**2 - 4*a*c) ** 0.5) / (2*a) 
x2 = (-b - (b**2 - 4*a*c) ** 0.5) / (2*a)

print(x1) # Answer for x1 should be "3"
print(x2) # Answer for X2 should be "-0.5"
