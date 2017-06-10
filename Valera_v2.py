names = []
print ('Provide your names: ')

your_command = input()
while your_command != "finish":
    names.append(your_command)
    print(' - confirmed\n\nTo complete the list tape "finish"')
    your_command = input("\nGive the next one: ")
    

print('The list is completed. You may start your research.\nInput the name: ')

your_name = input()
while your_name not in names:
    print("\nNot in the list. Try again!")
    your_name = input('\nProvide your name: ')

print(your_name, " has been found! \nHe is on the place number ", int(names.index(your_name)+1), " in the list." )