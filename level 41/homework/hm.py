#1)კომენტარის სახით ჩამოწერე თითეული სიის ფუნქცია.

#                                 ამოშლის ფუნქციები

# ჩვენ ვისწავლეთ .pop() ფრჩხილებში გადაეცემა ის ინდექსი რომლის ამოშლაც გვსურს სიიდან
# -- .remove() ფრჩხილებში გადაეცემა ის სიის ელემენტი რომლის ამოშლაც გვსურს სიიდან
#                                 ჩასმის ფუნქციები

# ჩვენ ვისწავლეთ .append() ფრჩხილებში გადავცემ იმ სიტყვას (ელემენტს) რაც მინდა რომ სიის "ბოლოში" დავამატო
# -- .insert( , ) ფრჩხილებში გადაეცემა ორი მონაცემი ჯერ ის თუ რომელ ინდექსზე გვინდა ჩამატება და შემდეგ ის თუ რა უნდა ჩავამატოთ

#2) სიის ბოლოში დავამატოთ რიცხვი 10
list=['nika' , 'gio ', 'luka' , '20' , '1.5 ', 'saxli']
list.append(10)
print(list)

#3)დავამატო ჩემი სახელი სიის ბოლოში
names=['gio' , 'luka' , 'saba' , 'giga' , 'mate']
names.append("nika")
print(names)

#4)მომხმარებელს შემოვატანინოთ სიტყვა და დავამატოთ სიის ბოლოში
names = ["Dato", "Giorgi", "Mariam"]
new_name = input("შეიყვანე რაიმე სახელი: ")
names.append(new_name)
print(names)

#5)სიაში 3 ინდექსზე დავამატოთ ჩემი სახელი
brothers=['luka' , 'mate' , 'gio' , 'saba']
brothers.insert(3,"nika")
print(brothers)

#6)სიაში ჩავამატოთ  მომხმარებლის მიერ არჩეულ ინდექსზე ელემენტი  
names = ["Ana", "Giorgi", "Nika", "Luka", "Mariam", "Dato"]
user_name = input("შეიყვანე სახელი: ")
user_index = int(input("შეიყვანე რიცხვი 0-დან 6-მდე: "))
names.insert(user_index, user_name)
print("განახლებული სია:", names)

#7)სიაში ჩავსვათ orange 1 ინდექსზე
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)

#8)სიაში ჩვსვათ ირაკლი ლუკას წინ
names = ["goga", "saba", "luka"]
names.insert(-1, "irakli")
print(names)

#9)insert() ფუნქციით ჩასვი "water" სიის დასაწყისში.
foods = ["bread", "milk", "cheese"]
foods.insert(0, "water")
print(foods)

#10)pop() ფუნქციით წაშალე ბოლო ელემენტი და დაბეჭდე განახლებული სია.
numbers = [5, 10, 15]
numbers.pop()
print(numbers)

#11)pop -ით ამოშალე "banana" და დაბეჭდე დარჩენილი სია.
fruits = ["apple", "banana", "orange"]
fruits.pop(1)
print(fruits)

#12)ამოშალე "saba" pop()-ით 
names = ["goga", "saba", "luka"]
names.pop(1)
print(names)

#13)op()-ით წაშალე "red" და დაბეჭდე განახლებული სია. შემდეგ სიიდან ასევე ამოშალე yellow
colors = ["red", "green", "blue", "yellow", "black", "purple"]
#1)
colors.pop(0)
print(colors)
#2)
colors.pop(2)
print(colors)

#14)pop ის დახმარებით სიიდან ამოშალე მომხმარებლის მიერ შემოტანილ რიცხვზე(ინდექსზე) მდგომი ელემენტი
num = int(input("შეიყვანე რიცხვი 0 დან 3 მდე: "))
items = ["pen", "pencil", "book", "eraser"]
items.pop(num)
print(items)

#15)remove() ფუნქციით სიისდან წაშალე "banana".
fruits = ["apple", "banana", "orange"]
fruits.remove("banana")
print(fruits)
#16)remove()-ით წაშალე 3 და დააკვირდი, მხოლოდ პირველი 3 იანი შაიშლება.
nums = [3, 5, 3, 7]
nums.remove(3)
print(nums)

#17)remove() ფუნქციით წაშალე "blue" და დაბეჭდე განახლებული სია.
colors = ["red", "blue", "green"]
colors.remove("blue")
print(colors)

#18)მომხმარებელს შემოატანინე სახელი და შემდეგ ისევ წაშალე
names = ["goga", "saba", "luka"]
name_input=input("რომელი სახელი ამოვშალო? (goga, saba, luka): ")
names.remove(name_input)
print(names)

#19)remove()-ით წაშალე "pencil" და დაბეჭდე დარჩენილი სია.
items = ["pen", "pencil", "book", "pencil"]
items.remove("pencil")
print(items)






