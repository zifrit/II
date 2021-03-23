import random as r


def cipher_3(text):
    cipher = {
        'А': ('В', '^'),
        'Б': ('И', '@'),
        'В': ('О', ')'),
        'Г': ('А', '+'),
        'Д': ('Щ', '<'),
        'Е': ('П', '>'),
        'Ж': ('К', '≎'),
        'З': ('Б', '⊽'),
        'И': ('Ъ', '⋼'),
        'К': (' ', '⋘'),
        'Л': ('Р', '⊄'),
        'М': ('Т', '≷'),
        'Н': ('Ц', '≉'),
        'О': ('.', 'ζ'),
        'П': ('Ж', 'ω'),
        'Р': ('Г', 'Ω'),
        'С': ('Л', 'Ψ'),
        'Т': ('Х', 'Σ'),
        'У': ('С', 'Ξ'),
        'Ф': ('Ь', 'ƃ'),
        'Х': ('Ч', '♥'),
        'Ц': ('З', '♧'),
        'Ч': ('М', '♦'),
        'Ш': ('У', '♮'),
        'Щ': ('Д', 'ø'),
        'Ъ': ('Э', '®'),
        'Ы': ('Н', '©'),
        'Ь': ('Ю', '™'),
        'Э': ('Ы', 'Ắ'),
        'Ю': ('Ш', 'Č'),
        'Я': ('Е', '₡'),
        ' ': ('Ф', 'ȡ'),
        '.': ('Я', 'ḩ♄')
    }
    trashcan1 = []
    for i in text:
        if i in cipher:
            nummber = r.randint(0, 1)
            trashcan1.append(cipher[i][nummber])
    b1 = ''
    for i in trashcan1:
        b1 = b1 + i
    b1.capitalize()

    trashcan2 = []
    for j in trashcan1:
        for n in cipher:
            if cipher[n][0] == j:
                trashcan2.append(n)
            elif cipher[n][1] == j:
                trashcan2.append(n)
    b2 = ''
    for i in trashcan2:
        b2 = b2 + i
    b2.capitalize()
    print(b1)
    print(b2)
    return trashcan1


def cipher_2(text='привет'):
    text = text.upper()
    cipher = {
        'А': '^',
        'Б': '@',
        'В': ')',
        'Г': '+',
        'Д': '<',
        'Е': '>',
        'Ж': '≎',
        'З': '⊽',
        'И': '⋼',
        'К': '⋘',
        'Л': '⊄',
        'М': '≷',
        'Н': '≉',
        'О': 'ζ',
        'П': 'ω',
        'Р': 'Ω',
        'С': 'Ψ',
        'Т': 'Σ',
        'У': 'Ξ',
        'Ф': 'ƃ',
        'Х': '♥',
        'Ц': '♧',
        'Ч': '♦',
        'Ш': '♮',
        'Щ': 'ø',
        'Ъ': '®',
        'Ы': '©',
        'Ь': '™',
        'Э': 'Ắ',
        'Ю': 'Č',
        'Я': '₡',
        ' ': 'ȡ',
        '.': 'ḩ♄'
    }
    trashcan1 = []
    for i in text:
        if i in cipher:
            trashcan1.append(cipher[i])
    b1 = ''
    for i in trashcan1:
        b1 = b1 + i
    b1.capitalize()

    trashcan2 = []
    for j in trashcan1:
        for n in cipher:
            if cipher[n] == j:
                trashcan2.append(n)
    b2 = ''
    for i in trashcan2:
        b2 = b2 + i
    b2.capitalize()
    print(b2)
    print(b1)
    return b2


def cipher_1(text='привет'):
    text = text.upper()
    cipher = {
        'А': ('В', 'Г'),
        'Б': ('И', 'З'),
        'В': ('О', 'А'),
        'Г': ('А', 'Р'),
        'Д': ('Щ', 'Щ'),
        'Е': ('П', 'Я'),
        'Ж': ('К', 'П'),
        'З': ('Б', 'Ц'),
        'И': ('Ъ', 'Б'),
        'К': (' ', 'Ж'),
        'Л': ('Р', 'С'),
        'М': ('Т', 'Ч'),
        'Н': ('Ц', 'Ы'),
        'О': ('.', 'В'),
        'П': ('Ж', 'E'),
        'Р': ('Г', 'Л'),
        'С': ('Л', 'У'),
        'Т': ('Х', 'М'),
        'У': ('С', 'Ш'),
        'Ф': ('Ь', ' '),
        'Х': ('Ч', 'Т'),
        'Ц': ('З', 'Н'),
        'Ч': ('М', 'Х'),
        'Ш': ('У', 'Ю'),
        'Щ': ('Д', 'Д'),
        'Ъ': ('Э', 'И'),
        'Ы': ('Н', 'Э'),
        'Ь': ('Ю', 'Ф'),
        'Э': ('Ы', 'Ъ'),
        'Ю': ('Ш', 'Ь'),
        'Я': ('Е', '.'),
        ' ': ('Ф', 'К'),
        '.': ('Я', 'О'),
    }
    trashcan1 = []
    for i in text:
        if i in cipher:
            trashcan1.append(cipher[i][0])
    b1 = ''
    for i in trashcan1:
        b1 = b1 + i
    b1.capitalize()

    trashcan2 = []
    for j in b1:
        if j in cipher:
            trashcan2.append(cipher[j][1])
    b2 = ''
    for i in trashcan2:
        b2 = b2 + i
    b2.capitalize()
    print(b2)
    print(b1)
    return b2


text = input().upper()
cipher_1(text)
cipher_2(text)
cipher_3(text)


