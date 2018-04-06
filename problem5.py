#Shauna Byrne  26/02/2018
#Project Euler Problem 5

answer = 20 #Sets value of answer to 20 for this test case           
repeat = True                
                             
while repeat:                
    repeat = False           
    for i in range(1, 20):   
        if (answer % i) != 0: #Checks if the remainder doesn't equal 0 when the number being checked is divided - divides answer in to i & says if the answer isn't 0 then don't print the answer yet & resets the loop to check the next number
            repeat = True    
            break #If remainder is not 0, resets loop to check next number           
                             
    if repeat:               
        #print answer        
        answer += 20         
                             
print (answer)
