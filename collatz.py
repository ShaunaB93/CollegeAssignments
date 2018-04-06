# Shauna Byrne 05.02.18
# Collatz Assessment

n = int(input("Please enter an integer: ")) #Requests the user to input a value to test

while (n > 0): #loops this code while the value inputted is greater than 0
    print (n) 
    if (n == 1): 
        break #Breaks loop if the integer is equal to 1
    elif (n % 2 == 0): #Continues with the following piece of code of integer is divisable by 2
        n = n // 2 #Divides the value of n by 2
    else:
        n = (n * 3 + 1) #Otherwise takes the vale of n & multiples by 3 then adds 1

