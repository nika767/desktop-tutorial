#1)
word = input("შეიყვანეთ სიტყვა: ")

# ვამოწმებთ არის თუ არა a/A
if 'a' in word or 'A' in word:
    print("არის ასო 'a' ან 'A'")
else:
    print("არ არის ასო 'a' ან 'A'")

# ვამოწმებთ არ არის თუ არა 'car'
if 'car' not in word:
    print("სიტყვა 'car' არ არის ტექსტში")
else:
    print("სიტყვა 'car' არის ტექსტში")




#2)
text = input("შემოიყვანე ტექსტი: ")

for i in text:
    if i == 'a' or i == 'A':
        continue
    print(i)
    