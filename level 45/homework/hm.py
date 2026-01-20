# 1)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
evens = []   
for i in numbers:        
    if i % 2 == 0:       
        evens.append(i)  
print(evens)  

# 2)
numbers = [3, 10, 5, 7, 12, 9, 15, 2, 21]
new_list = []
for i in range(len(numbers)):
    if i % 2 != 0:
        new_list.append(numbers[i])
print(new_list)

# 3)
names = ["გიგი", "ნიკა", "გაგა", "ლევანი", "გუკი", "თათია"]
for i in names:
    if i[0] == "გ" and i[-1] == "ი":
        names.remove(i)
print(names)

# 4)
words = ["Apple", "banana", "Cherry", "dog", "Elephant", "fish", "Grape"]
for i in range(len(words) - 1, -1, -1):
    if words[i][0].isupper():
        if i % 2 == 1: 
            words[i] = words[i].lower()
        else: 
            words.pop(i)
print(words)

# 5)
words = ["GameAB", "hello", "GoodXY", "python", "GreatZZ", "world", "GtestAA"]

for i in range(len(words) - 1, -1, -1):
    word = words[i]

    if word.startswith("G") and word[-2:].isupper():
        words.pop(i)

    elif word.islower():
        words[i] = word.upper()

print(words)

# 6)
