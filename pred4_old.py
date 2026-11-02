from math import *

a = 10
b = 20
c = 1000

D = b * b - 4 * a *c

#2roots
if D>0:
    x1 = (-b + sqrt(D)) / (2*a) 
    x2 = (-b - sqrt(D)) / (2*a) 
    print(x1, x2)
    
elif D==0:
    x1 = - 2 / (2*a)
    x2 = x1
    print(x1, x2)
    
else:
    print('No solution in R')
    