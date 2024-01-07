# Author: Sujal (Copied from https://github.com/Sujal092004/Repositories)
import time
import os

sum1 = 0



def select():
    print("select option from below :")
    options = ("1.)Addition\n", "2.)Substraction\n",
                "3.)Division\n", "4.)Multiplication\n", "5.)Mixed Calculation\n")
     for each_element in options:
        print(each_element)
        time.sleep(0.75)

    print("Enter your Choice : ", end="")
    option_choosed = int(input())

    if option_choosed == 1:
        addition()
        os.system('cls')
    elif option_choosed == 2:
        substraction()
        os.system('cls')
    elif option_choosed == 3:
        Division()
        os.system('cls')
    elif option_choosed == 4:
        Multiplication()
        os.system('cls')
    elif option_choosed == 5:
        mixed_calculation()
        os.system('cls')
    else:
        print("Invalid Input\n" + "Please,Try again ")
        select()
        os.system('cls')


def addition():
    global sum1
    addition_operand = input("Note: 1.) Enter your numbers and separate them with + \n"
                             "2.) In the end, press Enter for execution\n")
    addition_operands = addition_operand.split("+")
    sum1 = 0
    for operand in addition_operands:
        try:
            num = float(operand)
            sum1 += num
        except ValueError:
            print(f"Invalid input: {operand} is not a valid number")
            return
    os.system('cls')
    print(f"Your Enter Number is : {addition_operand}")
    print(f"Result: {sum1}")
    select()


def substraction():
    global sum1
    substraction_operand = input("Note: 1.) Enter your numbers and separate them with - \n2.) In the end, press Enter for execution\n")
    substraction_operands = substraction_operand.split("-")
    sum1 = substraction_operands[0]
    for num in substraction_operands[1:]:
        try:
            sum1 = float(sum1)
            num = float(num)
            sum1 -= num
        except ValueError:
            print(f"Invalid input: {num} is not a valid number")
    os.system('cls')
    print(f"Your Enter Number is : {substraction_operand}")
    print(f"Result: {sum1}")
    select()

def Division():
    global sum1
    division_operand = input("Note: 1.) Enter your numbers and separate them with / .\n2.) In the end, press Enter for execution.\n")
    division_operands = division_operand.split("/")
    sum1 = division_operands[0]
    for num in division_operands[1:]:
        try:
            sum1 = float(sum1)
            num = float(num)
            sum1 /= num
        except ValueError:
            print(f"Invalid input: {num} is not a valid number")
            return
    os.system('cls')
    print(f"Your Enter Number is : {division_operand}")
    print(f"Result: {sum1}")
    select()

def Multiplication():
    global sum1
    multiply_operand = input("Note: 1.) Enter your numbers and separate them with x. \n2.) In the end, press Enter for execution.\n")
    multiply_operands = multiply_operand.split("x")
    sum1 = 1
    for operand in multiply_operands:
        try:
            num = float(operand)
            sum1 *= num
        except ValueError:
            print(f"Invalid input: {operand} is not a valid number")
            return
    os.system('cls')
    print(f"Your Enter Number is : {multiply_operand}")
    print(f"Result: {sum1}")
    select()

def mixed_calculation():
    global sum1
    mixed_operand = input("Note: Enter your mixed calculation expression (e.g., 2+3*4/2) \n2.) After Entering press Enter Key: ")
    try:
        sum1 = eval(mixed_operand)
    except (SyntaxError, NameError):
        print("Invalid input: Please enter a valid mixed calculation expression.")
        return
    os.system('cls')
    print(f"Your Enter Expression is : {mixed_operand}")
    print(f"Result: {sum1}")
    select()

time.sleep(3)
#Author : Sujal
#Copied code from : Github
print("Starting Calculator", end=" ")
for i in range(6):
    time.sleep(1)
    print(".", end=" ")
os.system('cls')

print("Intializing Your Calculator", end=" ")
for i in range(6):
    time.sleep(1)
    print(".", end=" ")
os.system('cls')


select()



select()
