import numpy as np

# add()
# Returns element-wise string concatenation for two arrays of str or Unicode

char1 = np.array(['Hello ', 'Hi '])
char2 = np.array(['Rifat', 'Arefin'])

res = np.char.add(char1, char2)
print(res)


# multiply()
# Returns the string with multiple concatenation, element-wise

char1 = np.array("mahim")
res = np.char.multiply(char1, 3)
print(res)


#Capitalize()
char1 = np.array("hello mahim how are you")
res = np.char.capitalize(char1)
print(res)

#Title()
char1 = np.array("hello mahim how are you")
res = np.char.title(char1)
print(res)

#Upper()
char1 = np.array("mahim")
res = np.char.upper(char1)
print(res)

#Lower()
char1 = np.array("MAHIM")
res = np.char.lower(char1)
print(res)

#split()
str = np.array("hello how are you")
arr = np.char.split(str)
print(arr)

str = np.array("Mango, Jackfruit, Apple")
arr = np.char.split(str, sep=', ')
print(arr)

str = np.array("Mango\nJackfruit\nApple")
arr = np.char.split(str, sep='\n')
print(arr)

#splitlines() 
#Returns a list of the lines in the element, breaking at the line boundaries
#'\n', '\r', '\r\n' can be used as line boundaries.
str = np.array("Mango\nJackfruit\rApple")
arr = np.char.splitlines(str)
print(arr)

#join()
#This method returns a string in which the 
# individual characters are joined by separator character specified.
str = np.array('mahim')
print(np.char.join('-', str))
print(np.char.join(['-', ':'], str))
print(np.char.join(['-', ':'], ['dmy', 'ymd']))
print(np.char.join(['-', ':'], ['dmy', 'yymmdd']))

#replace()
str = np.array('mahim is a good boy')
print(np.char.replace(str, 'is', 'was'))