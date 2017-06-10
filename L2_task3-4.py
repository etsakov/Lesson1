import re
with open ('referat.txt', 'r', encoding='utf-8') as referat:
    content = referat.read()
    word_count = len(re.split('[ \n]', content))
    print(word_count)