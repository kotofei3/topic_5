fruits = dict(яблоко=50, банан=30, груша=40, апельсин=35)

print("Список фруктов и их цены:")
print(fruits)

user_input: str = input("Цена ")

print('-', fruits[user_input])
