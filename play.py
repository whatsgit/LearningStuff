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
##############################################
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
##############################################         
##Here is an example of a function named my_func. It takes no arguments, and prints "spam" three times. It is defined, and then called. The statements in the function are executed only when the function is called.
def my_func():
   print("spam")
   print("spam")
   print("spam")

my_func()
##############################################
##One argument function below##
def print_double(x):
   print(2 * x)

print_double(3)
##############################################
def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)
###############################################
def function(variable):
   variable += 1
   print(variable)

function(7)       ## returns a value of 8
#print(variable)   ##returns an error because variable is only defined inside the function

##############################################

##Any code after the return statement will never happen.
def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")

print(add_numbers(4, 5)) ##returns a value of 9

##############################################

def shout(word):
  """             ##Docstring
  Print a word with an
  exclamation mark following it.
  """             ##Docstring
  print(word + "!")
    
shout("spam")

##############################################

def add(x, y): 
  return x + y
"""
This feines the add() function
which has 2 arguments
"""
def do_twice(func, x, y):
  return func(func(x, y), func(x, y))
"""
This defines the do twice function which
has 3 arguments, a function and 2 integers
"""
a = 5
b = 10

print(do_twice(add, a, b)) ## so do twice calls add as the func a as the x and b as the y

##############################################

file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

##This will print all of the contents of the file "filename.txt".

##############################################

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()


##############################################

##After all contents in a file have been read, any attempts to read further from that file will return an empty string, because you are trying to read from the end of the file.

file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()

##############################################

file = open("newfile.txt", "w") ##opens/creates new txt file and assigns it to variable file "w" mode creates new if not there##
file.write("This has been written to a file")  ##invokes the write() method for the opened file
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()
##When a file is opened in write mode, the file's existing content is deleted.##
##############################################
##When a file is opened in write mode, the file's existing content is deleted.##

##When a file is opened in write mode, the file's existing content is deleted.##

##When a file is opened in write mode, the file's existing content is deleted.##

##When a file is opened in write mode, the file's existing content is deleted.##

##When a file is opened in write mode, the file's existing content is deleted.##

##When a file is opened in write mode, the file's existing content is deleted.##

##############################################

file = open("newfile.txt", "r")
print("Reading initial contents")   ## Not from the file##
print(file.read())                  ##Would  read what is in file##
print("Finished")
file.close()

##When a file is opened in write mode, the file's existing content is deleted.##

file = open("newfile.txt", "w")     ##This woudl delete what was previously in teh file##
file.write("Some new text")         ##write to $file##
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())                    ##shows contents of $file aka newfile.txt
print("Finished")
file.close()

##############################################









