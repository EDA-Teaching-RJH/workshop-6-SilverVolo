#Your code goes here. 

import math

def safe_divide(a, b):
    try:
        return(a/b)
    except ZeroDivisionError:
        print("Cannot divide by zero")

def process_list(input_list):
    sum = 0 
    for i in input_list:
        try:
            sum += input_list[i]
        except(TypeError,ValueError):
            print("Invalid input, skipping item")



def nested_operations(a, b):
    try:
        a = int(a)
        b = int(b)
        try:
            print( math.sqrt(a/b))
        except ZeroDivisionError:
            print("Can't divide by zero")
    except ValueError:
        print("Conversion Error")

def process_input():
    userInput = input("Input: ")
    try:
        userInput = float(userInput)
        square = userInput**2
    except:
        value = "None"
    else:
        print(square)
    finally:
        print("Processing complete.")


main()
