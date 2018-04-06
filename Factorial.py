#Shauna Byrne
#Exercise 6 code - 07/03/2018
#https://stackoverflow.com/questions/16683720/what-is-this-operator-1


def factorial(value):
    number = 1 #sets an original value for 'number'
    for i in range(1, value + 1): #loops to check each of the values between 1 and 'value' + 1.
        number *= i #each loop resets the value of number to equal 'number' * i
    return number #returns the value of 'number'

print("the factorial of 5 is", factorial(5))
print("the factorial of 7 is", factorial(7))
print("the factorial of 10 is", factorial(10))
