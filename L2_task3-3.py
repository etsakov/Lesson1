with open('referat.txt', 'r', encoding='utf-8') as file:
    mylist = file.readlines()
    print(mylist)

    count = line.split(' ')
    length = len(count)
    print(length, ' words in the phrase above')

# OR
 
    mylist = list(file)
    print(mylist)

    count = line.split(' ')
    length = len(count)
    print(length, ' words in the phrase above')



   
#    count = line.split(' ')
#    length = len(count)
#    print(length, ' words in the phrase above')
