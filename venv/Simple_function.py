def addition(a,b):
    return a+b

def reversing_string(string1):
    reversed_string = ""
    for iter in range(0, len(string1)):
        reversed_string = reversed_string + string1[len(string1) - 1 - iter]

    return reversed_string

