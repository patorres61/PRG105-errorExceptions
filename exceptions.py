# Phyllis Torres
# Exceptions assignment
# This program will attempt to open a file that does not exist and then handle the exception with an error message.
# It will also prompt for user input and then attempt to convert the input to an integer. If that fails, the
# program will handle the error with an error message.
# Due: 12/9/16

print 'Exception Handling'
print 'Phyllis Torres'
print 'Due: 12/9/16\n\n'

print 'The first task is to handle an error when attempting to read an input file that does not exist.\n\n'

fileIn = 'myfile.txt'

convertInput = 0

try:
    with open(fileIn, 'r') as f:
        file_content = f.read()
        print "Reading file: " + fileIn
    if not file_content:
        print "There is no data in file: " + fileIn
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror) + ': ' + fileIn
print "\nAnd now, onto the next task...\n\n"

print '\nThe second task is to handle an error when a user does not enter a valid integer.\n\n'

while True:
    try:
        userInput = raw_input("Please enter an integer: ")
        userInput = int(userInput)
        break
    except ValueError:
        print("\nThat is not a valid integer! Please try again...\n")
print "\nAwesome! You have successfully entered an integer!"

print "Thank you!"
