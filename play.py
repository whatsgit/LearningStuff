nums = list(range(5))
print(nums[4])

numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0, 20))

nums = list(range(5, 8))
print(len(nums))

print(list (range(8,3)))

numbers = list(range(5, 20, 2))
print(numbers)
#>>>
#[5, 7, 9, 11, 13, 15, 17, 19]
#>>>

words = ["hello", "world", "spam", "eggs"]
counter = 0 
max_index = len(words) - 1   ##This sets teh threshold for the counter to check against number of words minus one for the last item in the index

while counter <= max_index:
   word = words[counter]  ##prints the item at the index referenced by counter variable
   print(word + "!")
   counter = counter + 1  ##increments the counter up one index value.

##the for construct will run the iteration until it has hit the last item in the index without the need of a counter##
words = ["hello", "world", "spam", "eggs"]
for word in words:  ##for each word in the list of words do the following##
  print(word + "!")
  
for i in range(5):
   print("hello!")
  
for i in range(0, 20, 2):
   print(i)

for i in range(10):     ##for each item between 0 - 9
   if not i % 2 == 0:   ##If the remainder is not zero... 
      print(i+1)        ##...print that number plus 1
                        ## so prints all even numbers between 2 and 10
         
         
