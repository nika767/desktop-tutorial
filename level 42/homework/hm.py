# 1) შექმენი სია ხილებზე   მასში კიდევ 2 ხილი extend() ით დაამატე
fruits = ["ბანანი", "ანანასი", "ლიმონი"] 
fruits.extend(["ვაშლი", "მსხალი"])
print(fruits)

# 2)სია numbers ში დაამატე [40, 50] extend()-ით.

numbers = [1, 2, 3]
numbers.extend([40, 50])
print(numbers)

# 3)სია names  შეაბრუნე reverse()-ით.

names = ["giorgi", "likuna", "saba", "nuca"]
names.reverse()
print(names)

# 4)სია nums ში დათვალე რამდენი  5 არის

nums = [5, 5, 5, 5, 2, 5, 5]
count_5 = nums.count(5)
print(count_5)

# 5)letters = ["a","b","a","c"] დაბეჭდე რამდენი "a" არის სიაში.

letters = ["a","b","a","c"]
count_a = letters.count("a")
print(count_a)

# 6)სია names ში იპოვე "saba"-ს ინდექსი index()-ით.

names = ["giusha", "lamara", "vardosa", "saba"]
index_saba = names.index("saba")
print(index_saba)

# 7)list = ["red","green","blue"] რომელ ინდექსზე დგას "blue"

list = ["red", "green", "blue"]
index_blue = list.index("blue")
print(index_blue)

# 8) სია nums ში დამატე extend()-ით [7, 8, 9].

nums = [10, 12, 13, 24, 25, 36]
num = [7, 8, 9]
nums.extend(num)

# 9) სია foods ში დააბრუნე შებრუნებული სია.

foods = ["mwvadi", "xarcho", "ostri", "kababi"]  
reversed_foods = reversed(foods)
print(reversed_foods)

# 10) სია cities ში იპოვე რომელ ინდექსზე დგას "tbilisi".

cities = ["xoni", "terjola", "tbilisi", "zestafoni"]
index_tbilisi = cities.index("tbilisi")
print(index_tbilisi)

# 11)animals = ["cat","dog","cat","cow"] სიაში რამდენი "cat" არის

animals = ["cat","dog","cat","cow"]
count_cat = animals.count("cat")
print(count_cat)

# 12) სია fruits = ["apple", "banana"] დაამატე "grape".append() ით

fruits = ["apple", "banana"]
fruits.append("grape")
print(fruits)

# 13)numbers = [1, 2, 3] დაუმატე [4, 5] .extend() ით

numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)

# 14)names = ["goga", "saba"] ში insert()-ით ჩასვი "luka" პირველ ინდექსზე

names = ["goga", "saba"]
names.insert(1, "luka")
print(names)

# 15)items = ["pen", "pencil", "eraser"] pop()-ით წაშალე ბოლო ელემენტი

items = ["pen", "pencil", "eraser"]
items.pop("eraser")
print(items)

# 16)colors = ["red", "green", "blue"] remove()-ით წაშალე "green"

colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)

# 17)foods = ["bread", "milk"]. შეამოწმე სიაში 2 ელემენტია თუ მეტი — თუ ორია, append()-ით დაამატე "cheese", სხვა შემთხვევაში append()-ით დაამატე "meat"

foods = ["bread", "milk"]

if len(foods) == 2:
    foods.append("cheese")
else:
    foods.append("meat")

print(foods)

# 18)შექმენი სია nums = [10, 20, 30]. მომხმარებელს შემოატანინე მთელი რიცხვი. თუ რიცხვი nums სიაშია, დაბეჭდე "Already in list", თუ არა — append()-ით დაამატე 40 და დაბეჭდე სია.

nums = [10, 20, 30]
user_num = int(input("Enter number:"))
if user_num in nums:
    print("Already in list")
else:
    nums.append(40)
    print(nums)

# 19)შექმენი სია letters = ["a", "b", "c"]. მომხმარებელს შემოატანინე ასო, შემდეგ insert()-ით ჩასვი ის სიის შუაში (ცენტრალურ ინდექსზე). დაბეჭდე სია.
letters = ["a", "b", "c"]
user_letter = input("Enter a letter: ")
letters.insert(2, user_letter)
print(letters)
