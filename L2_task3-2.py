with open('text.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line)
        
    count = line.split(' ')
    length = len(count)
    print(length, ' words in the phrase above')
