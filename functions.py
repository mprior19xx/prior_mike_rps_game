# EXPLORING FUNCTIONS AND WHAT THE DO / HOW THEY WORK
# 
# EVERY DEFINITION NEEDS 2 BLANK LINES BEFORE AND AFTER
# 


def greeting():
    # say hello
	print("hello from your first function!")


# this is how you call / invoke a function
greeting()


def greetings(msg="hello player", num1=0):
    # creating another function with variable arguments
    print("Our function says", msg, "and also the number", num1)


myVariableNum = 0


# calling default argument for msg
greetings()
# these show up in place of msg and num
# these arguments do nothing outside of the function
greetings("This is an argument", 1)
greetings("Why are we arguing?", 2)


# function with math
def math(num2=2, num3=5):
    # global enlarges scope to use variable
    global myVariableNum

    myVariableNum = num2 + num3
    return num2 + num3


sum = math()
print("the sum of the numbers is:", sum)
print("the varial number is also:", sum)
