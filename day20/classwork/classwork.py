# 1)შექმენი ცვლადი,მიანიჭეთ ამ ცვლადს შემდეგი სტრინგი --> "ჰიდროელექტროსადგური" თქვენი დავალებაა გამოიტანოთ
# ამ სიტყვიდან პირველიდან
# 1 ინდექსიდან მე - 7 ინდექსამდე ელემენტები და ასევე კიდევ გამოიტანეთ ამ სტრინგიდან მე8 ინდექსიდან 16 - ე
# ინდექსამდე ელემენტები
# ბატონი გოგა ჩალაური — 6/29/2025 8:32 PM
# 2)1)შექმენი ცვლადი რომელსაც გადაეცემა პატარა ასოებით დაწერილი სტრინგი,შენი დავალებაა დააბრუნო
# ეს სტრინგი ოღონდ uppercase ში გადაყვანილი
#   2)შექმენი ცვლადი რომელსაც გადაეცემა  დიდი ასოებით დაწერილი სტრინგი,შენი დავალებაა დააბრუნო 
# ეს სტრინგი ოღონდ lowercase ში გადაყვანილი
#   3)შექმენი ცვლადი რომელსაც გადაეცემა პატარა ასოებით დაწერილი სტრინგი,შენი დავალებაა დააბრუნო
# ეს სტრინგი ისე რომ პირველი ასო იყოს დიდი
#   4)შექმენი ცვლადი რომელსაც გადაეცემა სტრინგი --> "კაიპურისჭამა" , შენი დავალებაა ამ სტრინგიდან 
# გაიგო რომელ ინდექსზე დგას ასო "ჭ" და ასო "პ"

name = "ჰიდროელექტროსადგური"
print(name[1:7])
print(name[8:16])

name = "nika"
lowercase = name.upper()
print(lowercase)

name ="NIKA"
upper = name.lower()
print(upper)

name = "nika"
lowercase = name.capitalize()
print(lowercase)

name = "კაიპურისჭამა"
index = name.find("ჭ")
print(index)
index = name.find("პ")
print(index)



