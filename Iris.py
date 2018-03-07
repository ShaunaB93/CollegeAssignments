#Shauna Byrne 03/03/18
#Iris Data - exercise 5

print("Petal Length", "|", "Petal Width", "|", "Sepal Length","|", "Sepal Width")
print("-"*60)
with open("data/iris.csv") as i:
 for line in i:
  k = (line.split(','))
  print(('{:14s} {:14s} {:14s} {:14s}').format(k[2], k[3], k[0], k[1])) #used 14 for alignment of numbers in output
