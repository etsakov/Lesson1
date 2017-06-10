text = input('tape any text here: ')

with open('text.txt', 'w', encoding='utf-8') as file:
    file.write(text)