days: list = ["Понедельник", "Вторник", "Среда",
              "Четверг", "Пятница", "Суббота", "Воскресенье"]

day_of_the_week: int = int(input('Введите номер дня недели от 1 до 7: '))
day = days[day_of_the_week - 1]
print(day)
