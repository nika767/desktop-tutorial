# 1)


words = ["hello", "World", "python", "Code", "linux"]

i = 0 
while i < len(words):
    if words[i].islower():
        words[i] = words[i].upper()
        i += 1
    else:
        words.pop(i)

print(words)



# 2)


text = "PyThOnLiNuX"
result = []

i = 0
while i < len(text):
    if text[i].isupper():
        result.append(text[i].lower())
    else:
        result.append(text[i].upper())
    i += 1

print(result)



# 3)


names = ["gio", "NIKA", "mari", "LUKA", "dato"]
result = []

for i in names:
    if i.islower():
        result.insert(0, i.upper())
    elif i.isupper():
        result.append(i.lower())

print(result)



# 4)

cities = ["TBILISI", "batumi", "KUTAISI", "zugdidi", "POTI"]
i = 0

while i < len(cities):
    if cities[i].isupper():
        cities.pop(i)
    else:
        cities[i] = cities[i].upper()
        i += 1

print(cities)



# 6)

symbols = []

for i in range(len(text)):
    if text[i].islower():
        symbols.append("+")

    elif text[i].isupper():
        symbols.append("-")

i = 0
i1 = symbols.count("-")

while i < len(symbols):
    if i1 % 2 == 0:
        if symbols[i] == "+":
            symbols.pop(i)
        else:
            i += 1
    else:
        if symbols[i] == "-":
            symbols.pop(i)
        else:
            i += 1

print(symbols)
        

# 8)

text = "Python is fun"

reversed_upper = ""

for i in reversed(text):
    reversed_upper += i.upper()

print(reversed_upper)