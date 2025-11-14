#1)
cities = ["Tbilisi", "Batumi", "London", "Amsterdam", "Kutaisi", "Berlin"]

for city in cities:
    if len(city) > 6:
        print(city)

#2)
words = ["awakwukulikolahjuki", "lukashiosnikastemos", "hello", "lolilikujylolik"]

for w in words:
    if len(w) % 15 == 0:
        print(w)

#3)
words = ["apple", "house", "phone", "cat", "music", "sport"]

for w in words:
    if len(w) == 5:
        print(w)

#4)
strings = ["hello", "programming", "world", "hypercommunication", "python"]

longest = ""   # აქ შევინახავთ ყველაზე გრძელს

for s in strings:
    if len(s) > len(longest):
        longest = s

print("ყველაზე გრძელი სტრინგი არის:", longest)




