#1)
word = input("შემოიყვანე სიტყვა: ")

for i in word:
    if i == 'e' or i == 'E':
        break
    print(i)


#2)
text = input("შემოიყვანე წინადადება: ")

if "bad" in text:
    print("აკრძალული სიტყვა!")
else:
    print("ყველაფერი რიგზეა")


#3)
sentence = input("შემოიყვანე წინადადება: ")

for c in sentence:
    if c == ' ':
        continue
    print(c)

#4)
text = input("შემოიყვანე წინადადება: ")

vowels = "aeiouAEIOU"

for ch in text:
    if ch in vowels:
        continue
    print(ch)

#5)
start = int(input("პირველი რიცხვი: "))
end = int(input("მეორე რიცხვი: "))

for num in range(start, end + 1):
    if num % 15 == 0:
        print("პირველი რიცხვი, რომელიც იყოფა 15-ზე:", num)
        break

#6)
while True:
    text = input("შემოიყვანე ტექსტი: ")

    if text == "python is best":
        break

    print("you should learn python")

#7)
start = int(input("პირველი რიცხვი: "))
end = int(input("მეორე რიცხვი: "))

count = 0

for num in range(start, end + 1):
    if num % 3 == 0:
        count += 1
        if count == 3:
            print("მესამე რიცხვი, რომელიც იყოფა 3-ზე:", num)
            break
    
    
    
    



