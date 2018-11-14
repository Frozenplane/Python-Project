print("Hello World!")
print('Hello World!')

# Cannot use a single quote because of the apostrofy in can't
print("I can't do it")
# Cannot use the double quote because of trying to make someone quote something
print('Scott sure "tries"')

# sscape charactor
print('This is the first line \nThis is the second line')

# printed integer and an integer string
print(35)
print('35')

# Concatenation combining strings
firstName = "Gaven"      # this is an inline comment
lastName  = "Allen"      # this stores the users lastname

print(firstName + " " + lastName)  # firstName lastName

    # Other Options
print(firstName,lastName)
print('{0} first name {1} last name'.format(firstName, lastName))
print('{1} first name {0} last name'.format(firstName, lastName))

# printing integers
firstNumber  = 5
secondNumber = 10
print(firstNumber + secondNumber)
print(firstNumber, secondNumber)
print('{0} is greater than {1}'.format(firstNumber, secondNumber))

# perfor math function
# floating number 3.1415926583265
highTestScore = 0.9372    # floating point number
lowTestScore  = 0.4598    # floating point number
print('The high score was ' + str(highTestScore) + '\nThe low score was ' + str(lowTestScore))
print('The high score was {0:.2f}\nThe low score was {1:.2f}'.format(highTestScore, lowTestScore))

print('The print a list of things'
    'Apple\n'
    'Bannana\n'
    'Orange\n')