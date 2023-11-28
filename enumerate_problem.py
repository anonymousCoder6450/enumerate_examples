# in this problem we're given a sequence of numbers that always add + 1, for example, 1,2,3,4,5 
#in the code you can see the list we use to call the function so
# We use a for loop to iterate through every single element and when it says i+ 1 you may think "it would go out of bounds and outside the list index
# But the [:-1] helps with that by going backward and preventing that. We use the enumerate function here to identify the index (which is i) and the value (which is this_num)

#the enumerate function helps us keep track of every iteration we make, providing the index and value

def first_non_consecutive(numbers):
    for i, this_num in enumerate(numbers[:-1]):
        next_num = numbers[i + 1]
        if next_num - this_num > 1:
            return next_num

#the purpose of sum is to first off the next_num is the number which is ahead of this_num so next_num - this_num would be the difference
# if the difference is greater than one then we return next_num and show where the gap is taking place (providing the value which is 7 in this case)

print(first_non_consecutive([1, 2, 3, 4, 5, 6, 8, 9]))

