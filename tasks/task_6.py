lines_one: str = input("Введите строку: ")

many_elements: set = set(lines_one)

print("Уникальные символы:", tuple(many_elements))
print("Количество уникальных символов:", len(many_elements))
