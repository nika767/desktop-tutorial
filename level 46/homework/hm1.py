# 1) 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in nums:  # ვუვლით ასლს
    if i % 2 == 0 or nums.index(i) % 2 !=0:
        nums.remove(i)

print(nums)

# 2)
words = ["apple", "banana", "cherry"]

for i in words[:]:
    words.append(i)

print(words)

#3) 
words = ["car", "bike", "bus"]
nums = [10, 25, 40, 55, 70]

for i in nums:
    if i > 20 and i < 50:
        words.append(str(i))

print(words)

# 4) 
words = ["apple", "Banana", "cherry", "Dog"]

for i in range(len(words)):
    first = words[i][0]
    if first == first.lower():
        words[i] = first.capitalize() + words[i][1:]

print(words)


# 5) 
# for ციკლი გამოიყენება იმისთვის, რომ ერთი და იგივე მოქმედება რამდენჯერმე შესრულდეს

# append() ამატებს  ელემენტს სიის დასასრულს

# remove() შლის სიიდან კონკრეტულ ელემენტს .

# pop() შლის ელემენტს ინდექსით და გვიბრუნებს მას.

# index() გვაჩვენებს ელემენტის ინდექსს  მოცემულ სიაში.

# len() გვაჩვენებს თუ რამდენი ელემენტია სიაში

# lower() ყველა ასოს სტრინგში აპატარავებს

# capitalize() სტრინგის პირველ ასოს ადიდებს
