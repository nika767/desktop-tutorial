# 1)

i = 1

for i in range(50):
    if i % 2 == 0:
        print(i,"ლუწი")
    else:
        print(i,"კენტი" )



# 2)

for i in range(20):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "იყოფა 3-ზე და 5-ზე")
    elif i % 3 == 0:
        print(i, "იყოფა 3-ზე")
    elif i % 5 == 0:
        print(i, "იყოფა 5-ზე")
    else:
        print(i, "არ იყოფა არცერთზე")


# 3)


i = int(input("Enter anu number:"))

for i in range(0,i):
    if i % 2 == 0:
        print(i,"x")
    else:
        print(i,"Y")



# 4)

numbers = [10, 25, 33, 47, 80, 99]

for i in numbers:
    if i > 50:
        print(i, "მეტი 50-ზე")
    else:
        print(i, "ნაკლები 50-ზე")



# 5)

sum_even = 0  

for i in range(100):  
    if i % 2 == 0:     
        print(i)
        sum_even += i   

print("ლუწი რიცხვების ჯამია:", sum_even)


# 6)
words = ["apple", "banana", "avocado", "pear", "Almond", "apricot", "grape"]

for w in words:
    if len(w) > 0 and w[0] == "a":
        print(w)



# 7).



for i in range(20): 
    if i == 0:
        print(i, "ნულია")
    elif i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")



# 8)

numbers = [5, 15, 25, 35, 45, 55]

for i in numbers:
    if i % 5 == 0:
        print(i)




# 9)
# მომხმარებელს შემოატანინე სიტყვა
word = input("შეიყვანე სიტყვა: ")

# for ციკლით დაბეჭდე თითოეული ასო ცალ-ცალკე

for i in word:
    print(i)



# 10)

total = 0

for i in range(1, 10):
    total += i

print("ჯამი არის:", total)