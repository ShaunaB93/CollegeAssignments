#Shauna Byrne  26/02/2018
#Project Euler Problem 5

answer = 20                  
repeat = True                
                             
while repeat:                
    repeat = False           
    for i in range(1, 20):   
        if (answer % i) != 0:
            repeat = True    
            break            
                             
    if repeat:               
        #print answer        
        answer += 20         
                             
print (answer)
