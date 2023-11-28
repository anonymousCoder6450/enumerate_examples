fruits = ["Apple", "Banana", "Tomato"]

#The one below just prints fruits automatically with a index and then the value (the words in the strings)
#it automatically provides you with the index and value since there isn't a defined one
print(list(enumerate(fruits)))

#The one below now prints the fruit with the print function printing
#every element and the corresponding index on a new line as well as a fruit value defined
for fruit in enumerate(fruits):
    print(fruit)


#This time we already have our index and the fruit which is defined and instead of having any parentheses it just says
#"0 Apple" which is way cleaner and can help when returning specific things (tuple, list, string, etc)
for index, fruit in enumerate(fruits):
    print(index, fruit)
