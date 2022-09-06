# use quotation marks for defining sting
"Michel Jackson"

# use single quotation marks for defining string
'Michel Jackson'

# digitals and space in string
'1 2 3 4 5 6'

# special characters in string
'@#2_$#%#$%$&%'

# print the string
print('hello!')

# assign string to variable
name = "Michael Jackson"
print(name[0])

# print the element on index 6 in the string
print(name[6])

# print the element on the 13th index in the string
print(name[13])

# print the last element in the string
print(name[-1])

# print the first element in the string
print(name[-15])

# find the lenth of string
print(len(name))

# take the slice on variable name with only index 0 to index 3
print(name[0:4])

# take the slice on variable with only index 8 to index 11
print(name[8:12])

# get every second element. The elements on index 1, 3, 5 ...
print(name[::2])

# get every second element in the range from index 0 to index 4
print(name[:5:2])

# concatenate two strings
statement = name + 'is the best'
print(statement)

# print the string for 3 times
print(3*statement)

# concatenate strings
name = "Michael Jackson"
name += " is the best"
print(name)

# new line escape sequence
print(" Michael Jackson \n is the best")

# tab escape sequence
print(" Michael Jackson \t is the best")

# include back slash in string
print(" Michael Jackson \\ is the best")

# convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("after upper:", b)

# replace the old substring with the new target substring is the segment has been found in the string
a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
print(b)

# find the substring in the string. Only the index of the first element of substring in string will be the output
name = "Michael Jackson"
print(name.find('Jack'))

# if cannot find the substring in the string
name.find('Jasjbasdlfb')

# write tout code bellow and press Shift+Enter to execute
a = "1"

print('\\')