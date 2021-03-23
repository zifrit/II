text = 'привет'
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
