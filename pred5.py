#Factorial: 5 * 4 * 3 * 2
n = 5
fn = 1

while n > 1:
    #Compute factorial
    fn = n * fn
    
    #Decrement n
    n = n - 1

print(fn)

#Factorial: 2 * 3 * 4 * 5
i = 2
n = 5
fn = 1

while i <= n:
    #Compute factorial
    fn = i * fn
    
    #Increment i
    i = i + 1
    
print(fn)   

#Find maximum
M = [3.9, 4.7, 2.5, 3.9, 5.1, 1.9]

#Initialize maximum
m_max = M[0]

#Process items one by one
for m in M:
    #Actualize maximum
    if m > m_max:
        m_max = m
        
print(m_max)

#Find maximum and minimum
m_max = M[0]
m_min = M[0]

#Process items one by one
for m in M:
    #Actualize maximum
    if m > m_max:
        m_max = m
    
    #Actualize minimum
    if m < m_min:
        m_min = m
    
print(m_min,m_max)

#Find maximum and minimum, optimized
m_max = M[0]
m_min = M[0]

#Process items one by one
for m in M:
    #Actualize maximum
    if m > m_max:
        m_max = m
    
    #Actualize minimum
    else:
        m_min = m
    
print(m_min,m_max)

#Modify list
L = [1, 3, 5, 7, 9]
L2 = L

for l in L2:
    l = 10 * l

L2 = [10 * l for l in L]

#Ranges
R = range(0, 10, 1)
R = range(10, 60, 10)

for r in R:
    print(r)
    
#Find maximum and minimum, browse indices
m_max = M[0]
m_min = M[0]

#Process items one by one
for i in range(len(M)):
    #Actualize maximum
    if M[i] > m_max:
        m_max = M[i]
    
    #Actualize minimum
    else:
        m_min = M[i]
        
#Find maximum and minimum, indices of min and max
i_max = 0
i_min = 0
m_max = M[i_max]
m_min = M[i_min ]

#Process items one by one
for i in range(1, len(M)):
    #Actualize maximum
    if M[i] > m_max:
        m_max = M[i]
        i_max = i
    
    #Actualize minimum
    else:
        m_min = M[i]
        i_min = i

print(m_min, m_max, i_min, i_max,)

#Find x in X
X = [1, 3, 5, 7, 12, 51, 2026, 1, 3]

x = 3
i_x = -1

for i in range(len(X)):
    
    #Compare
    if (x == X[i]):
        i_x = i
        break
#Print
if i_x > -1:        
    print('Found, Index=', i_x)
else:
    print('x not in X')
        
