#21)
pets = ["cat", "dog", "hamster"]
name = input("შეიყვანე შინაური ცხოველის სახელი: ")
if name in pets:
    pets.remove(name)
    print("Removed")
else:
    print("Not found")

print(pets)

#22)
pets = ["cat", "dog", "hamster"]
name = input("შეიყვანე შინაური ცხოველის სახელი: ")
if name in pets:
    pets.remove(name)
    print("Removed")
else:
    print("Not found")

print(pets)

#23)
num = ["first", "second"]

new_item = input("შემოიტანე ახალი ელემენტი: ")

num.insert(0, new_item)

if len(num) > 5:
    num.pop()
    print(num)
else:
    num.reverse()
    print(num)

#24)
nums = [2, 4, 6]
num = int(input("შეიყვანე რიცხვი: "))
if num > 0:
    nums.append(num)
else:
    print("Only positive allowed")

print(nums)

#25)
mix = ["x", "y", "z"]
mix.extend([1, 2, 3])
letter = input("შეიყვანე ასო: ")
if letter in mix:
    mix.remove(letter)
    print("Removed")
else:
    print("No such element")

print(mix)


