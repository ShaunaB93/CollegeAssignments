#Shauna Byrne 03/03/18
#Iris Data - exercise 5

print("Petal Length", "|", "Petal Width", "|", "Sepal Length","|", "Sepal Width") #Prints heading line added for visual effect on output
print("-"*60)#Prints dividing line added for visual effect on output
with open("data/iris.csv") as i: #Opens csv file containing data set
 for line in i:
  k = (line.split(',')) #splits the information from the file
  print(('{:14s} {:14s} {:14s} {:14s}').format(k[2], k[3], k[0], k[1])) #used 14 for alignment of numbers in output
