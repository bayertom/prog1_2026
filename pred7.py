from math import *

#Recursion
def f(n):
    print("C(" + str(n)+")")
    if (n == 1):
        print("D");
    else:
        print("f(" + str(n-1) + ")")
        f(n - 1)
    print("E(" + str(n) + ")")
    
def fact(x):
    #Non-recursive solution
    if x == 1:
        return 1
    
    #Recursive call
    else:
        return x * fact(x-1)
    
def fact2(x):
    #Recursive call
    if x > 1:
        return x * fact2(x-1)
    
    #Non-recursive solution
    else:
        return 1
    
def fib(n):
    #Non recursive solution
    if n<=1:
        return 1
    
    #2 recursive calls
    else:
        return fib(n-1)+fib(n-2)
    
def g(x):
    
    if x == 1:
        return 1
    
    #Recursive call
    else:
        return x * g(x-2)
    
def maxi(X, l, r):
    
    #Non recursive solution
    if r <= l+1:
        return max(X[l], X[r])
    
    #recursion
    else:
        #mid index
        m = (l+r)//2
        
        #Left maximum
        lmax = maxi(X, l, m)
        
        #Right maximum
        rmax = maxi(X, m+1, r)
        
        #Max of both
        return max(lmax, rmax)
    
def bsearch(X, l, r, a):
    #Non recursive solution
    if r < l:
        return -1
        
    #Recursion:
    else:
        #Median
        m = (l+r)//2

        #Mid point
        if X[m] == a:
            return True
        
        #Left interval
        elif a < X[m]:
            return bsearch(X, l, m-1, a)
        
        #Right interval
        else:
            return bsearch(X, m+1, r, a)      

f(3)

#factorial
y = fact(3)

#Fibonacci
y = fib(4)

#Wrong construcion of condition
y = g(3)

#Find max
X = [1, 2, 3, 40, 56]
xmax = maxi(X, 0, len(X)-1)
print(xmax)

#Binary search
fnd = bsearch(X,0, len(X)-1, 40)
print(fnd)