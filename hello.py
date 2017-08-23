# This program says hello and asks for my name.

print('Hello World!')
print('What is your name?') #ask for their name
myName = input()
print('It is good to meet you, ' + myName)
myNameLength = (len(myName))
print('Your name is ' + str(myNameLength) + ' letters long')
print('What is your age?') #ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
