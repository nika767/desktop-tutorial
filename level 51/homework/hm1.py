# 1)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divided = []

for i in num:
    divided.append(i*2)
print(divided)



#2)

name = ["gaga", "gega", "giga", "guga", "goga"]
added = int(input(" To add name 'nika' enter index between 0-4:"))

name.insert(added,"nika")

print(name)



# 3)

word = "Python programming is fun"
vowels = "aeiouAEIOU"

for i in word:
    if i in vowels:
        print(i)




#4)


words = ["car", "python", "sun", "hello", "sky", "program", "cat"]

for i in words:
    if len(i) > 4 or words.index(i) % 2 != 0:
        words.remove(i)

print(words)




# 5)

numbers = [2, 4, 6, 8, 10]

total = 0

for i in numbers:
    total += i

average = total / len(numbers)
print(average)