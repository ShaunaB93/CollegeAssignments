# Shauna Byrne 05.02.18
# Collatz Assessment

n = int(input("Please enter an integer: "))

while (n > 0):
    print (n)
    if (n == 1):
        break
    elif (n % 2 == 0):
        n = n // 2
    else:
        n = (n * 3 + 1)

