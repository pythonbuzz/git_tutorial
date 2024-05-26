import math
print(math.factorial(5))  # with buitlin function

def fact(n):
    
    count = 1
    for i in range(n,0,-1):
        
        count = count * i
        
    print(count)        

fact(5)


