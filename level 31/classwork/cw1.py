# 1)შექმენით სია -->  ["ina" , "givi" , "nika" , "daviti" , "ia" , "lizi"] , თქვენი დავალებაა რომ პირველი 2 ელემენტი ჩაანაცვლოთ შემდეგი სიით
#  --> ["irina" , "milana" , "kira", "mate"] //////////////// და ასევე სიის ბოლო ორი ელემენტი შეანაცვლე შემდეგი სიით
#   --> ["gia" , "emzari" , "xvicha"] ამის შემდეგ დაპრინტეთ საბოლოო სია


#---------
names = ["ina", "givi", "nika", "daviti", "ia", "lizi"]

# ------------
names[0:2] = ["irina", "milana", "kira", "mate"]

# -------------
names[-2:] = ["gia", "emzari", "xvicha"]

# -----------
print(names)


# 2)
#---------

#------------
num = int(input("შეიყვანეთ რიცხვი: "))

# ---------
if num % 2 == 0:
    print("even")
else:
    print("odd")