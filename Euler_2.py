s = 2
a1 = 1
a2 = 2
a3 = 3

while a3<=4000000:    
    if a3%2 == 0:
        s=s+a3
    
    a1=a2
    a2=a3
    a3=a1+a2
    continue
    
print (s)
        
    
