# 1)

names = ["Gio", "mari", "tekla", "nika", "lizi"]
Upper_name = []

for name in names:
    if name[0] == name[0].upper():
        Upper_name.append(name)

print(Upper_name)


# 2)

names = ["gio", "tekla", "mari"]
surnames = ["BERIDZE", "ZARNADZE", "GIGASHVILI"]

for i in range(len(names)):
    names[i] = names[i].upper()

for i in range(len(surnames)):
    surnames[i] = surnames[i].lower()

result = names + surnames

print(result)


# 3)

words = ["APPLE", "banana", "CherryA", "orange", "DOG", "Elephant"]

for i in words:
    if len(i) < 6 or i[-1] == i[-1].upper():
        words.remove(i)

print(words)


# 4) 

nums = [5.5, 12.3, 9.8, 45.6, 101.2, 78.9, 10.1, 99.9, 150.0, 20.0]
filtered = []

for n in nums:
    if n > 10 and n < 100:
        filtered.append(n)

print(filtered)


# 5) 

cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Gori"]
countries = ["Georgia", "France", "Italy", "Spain", "Germany","USA", "Canada", "Japan", "China", "Brazil"]

index = 0

for c in cities:
    countries.insert(index, c)
    index += 1

print(countries)