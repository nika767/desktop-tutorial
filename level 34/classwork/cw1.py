# 1)

text = input("შეიყვანე სიტყვა ან ტექსტი: ")

print("სიგრძე:", len(text))

for letters in text:
    print(letters)


# 2)


words = ["კომპიუტერი", "მზე", "სიყვარული", "ცხვარი", "წიგნი"]

for word in words:
    length = len(word)
    print(f"სიტყვა: {word} -> სიგრძე: {length}")

    if length % 2 == 0:
        print("ლუწია")
    else:
        print("კენტია")