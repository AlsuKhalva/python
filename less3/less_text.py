with open('referat.txt', 'r', encoding='utf-8') as referat:
    content = referat.read()
    content = content.replace('\n', ' ')
    print(len(content))
    # print(content)

    content_word = content.split()
    # print(content_word)
    print(len(content_word))

    content = content.replace('.', '!')
    print(content)

    with open('referat2.txt', 'w', encoding='utf-8') as referat2:
        referat2.write(content)
