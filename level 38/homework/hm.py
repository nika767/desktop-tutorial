#1)
name = input("შეიყვანე სახელი: ")
print(name.upper())
#2)
name = input("შეიყვანე სახელი (დიდი ასოებით): ")
print(name.lower())
#3)
name = input("შეიყვანე სახელი (პატარა ასოებით): ")
print(name.capitalize())
#4)
names = ["dato", "nika", "luka", "ana"]

for n in names:
    print(n.upper())
#5)
names = ["DATO", "NIKA", "LUKA", "ANA"]

for n in names:
    print(n.lower())
#6)
names = ["dato", "nika", "luka", "ana"]

for n in names:
    print(n.capitalize())
#7)
items = ["a", "b", "c", "d", "e"]
print(len(items))
#8)
text = "ალექსანდრე"
print(len(text))
#9)
numbers = [1, 2, 4, 7, 10, 13, 16]

count_even = 0
for num in numbers:
    if num % 2 == 0:
        count_even += 1

print("ლუწი რიცხვების რაოდენობა:", count_even)
#10)
numbers = [1, 2, 4, 7, 10, 13, 16]

count_odd = 0
for num in numbers:
    if num % 2 != 0:
        count_odd += 1

print("კენტი რიცხვების რაოდენობა:", count_odd)
#11)
start = int(input("start: "))
end = int(input("end: "))
step = int(input("step: "))

for num in range(start, end, step):
    if num % 2 == 0:
        print(num)
