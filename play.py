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
##An expression is tested, and if the result comes up false, an exception is raised.
##Assertions are carried out through use of the assert statement.

print(1)			##prints
assert 2 + 2 == 4	##does not print but but is true so program continues to run
print(2)			##prints
assert 1 + 1 == 3	##returns an assertion error and ends program
print(3)			##never prints

##The assert can take a second argument that is passed to the AssertionError raised if the assertion fails. 
temp = -10
assert (temp >= 0), "Colder than absolute zero!"	##AssertionError: Colder than absolute zero!##

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
##The write() method returns the number of bytes written to a file, if successful.##
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

##If a file write operation is successful, which one of these statements will be true?##
##file.write(msg) == len(msg)##

##############################################

##It is good practice to avoid wasting resources by making sure that files are always closed after they have been used. One way of doing this is to use try and finally.##
try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()

##An alternative way of doing this is using with statements. This creates a temporary variable (often called f), which is only accessible in the indented block of the with statement.##

with open("filename.txt") as f:
   print(f.read())

##############################################

##The None object is used to represent the absence of a value.##

>>> None == None
True
>>> None
>>> print(None)
None
>>>

##The None object is returned by any function that doesn't explicitly return anything else. ##
def some_func():
   print("Hi!") 		##prints Hi!##

var = some_func()
print(var)				##returns None##

##############################################

##Dictionaries are data structures used to map arbitrary keys to values.
##Lists can be thought of as dictionaries with integer keys within a certain range.
##Dictionaries can be indexed in the same way as lists, using square brackets containing keys.
##Each element in a dictionary is represented by a key:value pair.
##An empty dictionary is defined as {}.

ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"]) ##prints 24
print(ages["Mary"]) ##prints 42

##Trying to index a key that isn't part of the dictionary returns a KeyError.

primary = {
  "red": [255, 0, 0], 
  "green": [0, 255, 0], 
  "blue": [0, 0, 255], 
}

print(primary["red"])		##prints [255,0,0]
print(primary["yellow"])	##returns KeyError:'yellow'

##Only immutable objects can be used as keys to dictionaries. Immutable objects are those that can't be changed. So far, the only mutable objects you've come across are lists and dictionaries. Trying to use a mutable object as a dictionary key causes a TypeError. 

bad_dict = {
  [1, 2, 3]: "one two three",  ##returns TypeError: unhashable type: 'list'
}

##Just like lists, dictionary keys can be assigned to different values.
##However, unlike lists, a new dictionary key can also be assigned a value, not just ones that already exist. 

squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)    ##result {8: 64, 1: 1, 2: 4, 3: 9, 4: 16}

#SO after reading the comments am I understanding this right? The squares[3] assignment could have just as likely changed 4: 16 to 4: 9 instead of 3: "error" to 3: 9 if it had placed {1: 1, 2: 4, 3: 9, 4: 16, 8: 64} instead of {8: 64, 1: 1, 2: 4, 3: 9, 4: 16} ? Or is the key the literal indexed position and "error" would have been replaced regardless of its place in the dictionary... this opposed to list indexing up from [0] ...

#To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.

nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

>>>
True
False
True
>>>

#A useful dictionary method is get. It does the same thing as indexing, but if the key is not found in the dictionary it returns another specified value instead ('None', by default).

pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

>>>
[2, 3, 4]
None
not in dictionary
>>>

##############################################
###Tuples#####################################
##############################################

##Tuples are very similar to lists, except that they are immutable (they cannot be changed).
##Also, they are created using parentheses, rather than square brackets. 

words = ("spam", "eggs", "sausages",)

##You can access the values in the tuple with their index, just as you did with lists:

print(words[0])

##Trying to reassign a value in a tuple causes a TypeError.

words[1] = "cheese"

>>>
TypeError: 'tuple' object does not support item assignment
>>>

##Like lists and dictionaries, tuples can be nested within each other.
##Tuples can be created without the parentheses, by just separating the values with commas.
##Tuples are faster than lists, but they cannot be changed.

my_tuple = "one", "two", "three"
print(my_tuple[0])
>>>
one
>>>

##An empty tuple is created using an empty parenthesis pair.
tpl = ()

# list
list = ["one", "two"]


# dictionary 
dict = {1:"one", 2:"two"}


# tuple 
tp = ("one", "two")



##############################################
###List Slices################################
##############################################

##List slices provide a more advanced way of retrieving values from a list. Basic list slicing involves indexing a list with two colon-separated integers. This returns a new list containing all the values in the old list between the indices.
##Like the arguments to range, the first index provided in a slice is included in the result, but the second isn't.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

>>>
[4, 9, 16, 25]
[9, 16, 25, 36, 49]
[0]
>>>

##If the first number in a slice is omitted, it is taken to be the start of the list.If the second number is omitted, it is taken to be the end. 
##Slicing can also be done on tuples.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

>>>
[0, 1, 4, 9, 16, 25, 36]
[49, 64, 81]
>>>

##List slices can also have a third number, representing the step, to include only alternate values in the slice. [2:8:3] will include elements starting from the 2nd index up to the 8th with a step of 3.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

>>>
[0, 4, 16, 36, 64]
[4, 25]
>>>

##Negative values can be used in list slicing (and normal list indexing). When negative values are used for the first and second values in a slice (or a normal index), they count from the end of the list.
##Remember, 0 denotes counting from left, whereas counting from right begins with a -1. If a negative value is used for the step, the slice is done backwards. Using [::-1] as a slice is a common and idiomatic way to reverse a list.


squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

>>>
[1, 4, 9, 16, 25, 36, 49, 64]
>>>

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])
>>>
[49, 36] 
>>>


##############################################
###List Comprehension#########################
##############################################

##List comprehensions are inspired by set-builder notation in mathematics.
##List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule. For example, we can do the following: 
cubes = [i**3 for i in range(5)]
print(cubes)
>>>
[0, 1, 8, 27, 64]
>>>
##range 5 means from 0 to 4 
##giving (0, 1, 2, 3, 4.) making 5 in total. 
##and the key is x**3. 
##so;
##    0**3= 0×0×0= 0 
##    1**3= 1×1×1= 1 
##    2**3= 2×2×2= 8 
##    3**3= 3×3×3= 27 
##    4**3= 4×4×4= 64

nums = [i*2 for i in range(10)]
>>>
A list of even numbers between 0 and 18
>>>

##A list comprehension can also contain an if statement to enforce a condition on values in the list.
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)
>>>
[0, 4, 16, 36, 64]
>>> 

##You can add as many 'if's as you want! 
evens=[i**2 for i in range(10) if i**2 % 2 == 0 if i**2 % 3 == 0] 
print(evens)
>>>
[0, 36]
>>>


##Create a list of multiples of 3 from 0 to 20.
a = [i for i in range(20) if i%3==0]

##Trying to create a list in a very extensive range will result in a MemoryError. This code shows an example where the list comprehension runs out of memory. This issue is solved by generators, which are covered in the next module.
even = [2*i for i in range(10**100)]
>>>
MemoryError
>>>

##create a list of numbers multiplied by 10 in the range of 5 to 9.

a = [x*10 for x in range(5 , 9)]


##############################################
###String Formatting##########################
##############################################

##So far, to combine strings and non-strings, you've converted the non-strings to strings and added them. String formatting provides a more powerful way to embed non-strings within strings. String formatting uses a string's format method to substitute a number of arguments in the string.

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)
			##Each argument of the format function is placed in the string at the corresponding position, which is determined using 			the curly braces { }.
>>>
Numbers: 4 5 6
>>>

print("{0}{1}{0}".format("abra", "cad"))
>>>
abracadabra
>>>

##String formatting can also be done with named arguments.
a = "{x}, {y}".format(x=5, y=12)
print(a)
>>>
5, 12
>>>


##############################################
###Useful Functions ##########################
##############################################

##Python contains many useful built-in functions and methods to accomplish common tasks.
##join - joins a list of strings with another string as a separator.
##replace - replaces one substring in a string with another.
##startswith and endswith - determine if there is a substring at the start and end of a string, respectively.
##To change the case of a string, you can use lower and upper.
##The method split is the opposite of join, turning a string with a certain separator into a list.

print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

##To find the maximum or minimum of some numbers or a list, you can use max or min.
##To find the distance of a number from zero (its absolute value), use abs.
##To round a number to a certain number of decimal places, use round.
##To find the total of a list, use sum.

print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))
>>>
0
9
99
42
15
>>>

a = min([sum([11,22]), max(abs(-30), 2)])
print(a)
>>>
30
>>>

##Often used in conditional statements, all and any take a list as an argument, and return True if all or any (respectively) of their arguments evaluate to True (and False otherwise).
##The function enumerate can be used to iterate through the values and indices of a list simultaneously.

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

for v in enumerate(nums):
   print(v)

>>>
All larger than 5
At least one is even
(0, 55)
(1, 44)
(2, 33)
(3, 22)
(4, 11)
>>>

filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()

print(text)


##This part of the program shows a function that counts how many times a character occurs in a string. def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count
##This function takes as its arguments the text of the file and one character, returning the number of times that character appears in the text.
##Now we can call it for our file. filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()

print(count_char(text, "r"))
>>>
Enter a filename: test.txt
83
>>>

##This is an example project, showing a program that analyzes a sample file to find what percentage of the text each character occupies.
##This section shows how a file could be open and read. filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()

print(text)

