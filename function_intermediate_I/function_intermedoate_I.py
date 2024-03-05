import random
def randInt(min= 0 , max= 100 ):
    if min > max:
        min, max = max, min
    return round(random.random() * (max - min) + min)

print(randInt())           
print(randInt(50))        
print(randInt(max=50))     
print(randInt(10, 50))    
print(randInt(50, 10))   
