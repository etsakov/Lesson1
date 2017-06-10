with open('text.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

    count = content.split(' ')
    length = len(count)
    print(length, ' words in the phrase above')
