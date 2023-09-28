fruits: dict = dict(яблоко=50, банан=30, груша=40, апельсин=35)

print("Список фруктов и их цены:")
print(fruits, end='\n\n')

user_input: str = input("Выберите фрукт из списка: ")

print('Цена', user_input, '-', fruits[user_input])
