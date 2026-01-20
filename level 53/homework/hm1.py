words = ["giorgi", "GOGA", "Nika", "gurgena", "Hello", "Natali", "tato"]
new_list = []
for w in words:
    if w.islower() and w[0] == "g":
        new_list.append("Goga")
    elif w.isupper() or w[0] == "N":
        new_list.append("Nika")
    else:
        new_list.append("ლიდერი")
print(new_list)



# 3) 
nums = [5, 6, 7, 8, 9, 10]
new_list = []
i = 0
while i < len(nums):
    if nums[i] % 2 == 0 or i % 2 == 0:
        new_list.append(nums[i] ** 2)
    else:
        new_list.append(nums[i] * 2)
    i += 1
print(new_list)

# 4)
i = 0
while i < len(words):
    if len(words[i]) > 6 or words[i].isupper():
        new_list.append(words[i].lower())
    else: 
        new_list.append(words[i] * 2)
    i += 1
print(new_list)


# 5) 
#task1)
numbers = "0123456789"
new_list = []
for i in range(len(numbers)):
    digit = int(numbers[i])
    if i % 2 == 0 or digit > 7:
        new_list.append(digit)
print(new_list)

#task2)

numbers = "0123456789"
new_list = []

i = 0
while i < len(numbers):
    digit = int(numbers[i])
    if i % 2 == 0 or digit > 7:
        new_list.append(digit)
    i += 1

print(new_list)