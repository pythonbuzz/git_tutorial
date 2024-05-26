import math
print(math.factorial(5))  # with buitlin function

def fact(n):
     
     if n <=0:
         print("factorial is less than 1 please provide appropriate number")
         
     elif n==1:
        print(f"factorial of {n} is 1")
     else:
        count = 1
        for i in range(n,0,-1):
            
            count = count * i
            
        print(count)        

fact(5)


