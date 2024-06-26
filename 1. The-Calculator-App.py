#Task 1
def addition():
    if input1 == "addition":
        final_num = num1 + num2
        print(final_num)
def subtraction():
    if input1 == "subtraction":
        final_num = num1 - num2
        print(final_num)
def multipliction():
    if input1 =="multiplication":
        final_num = num1 * num2
        print(final_num)
def division():
    if input1 =="division":
            if num2 != 0:
                final_num = num1 / num2
                print(final_num)
            else:
                print("The awnser is zero ")

#Task 2
num1 = int(input("What is the first number you would like to use? " ))
num2 = int(input("What is the second number you would like to use? " ))
input1 = input("What would you like to do with the two numbers? addition, subtraction, multiplication, division " )


if input1 == "addition":
    addition()
elif input1 == "subtraction":
    subtraction()
elif input1 == "multiplication":
    multipliction()
else:
    division()

#Task 3
# Look at line 15 through 17 in def division(). I added a clause in the base code.