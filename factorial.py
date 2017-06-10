user_input = int(input('Give a number to calculate factorial: '))
fac = 1
termination_point = 0

while user_input > termination_point:
    termination_point += 1
    fac = fac * termination_point

print ("\nHere is your result: ", fac)