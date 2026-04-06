# TODO решите задачу
import json
def task() -> float:
    summa = 0 # задаем начальную сумму 0
    with open("input.json" ) as file: # открывает файл со словарями
        data = json.load(file) # записываем в переменную его считанные данные
        for para in data: # проходим по каждому отдельному словарю
            # находим значение произведения по парам ключ-значение типа float
            proiz = float(para["score"]) * float(para["weight"])
            summa += proiz # добавляем к начальной сумме каждый раз полученное значение произведения
        return round(summa, 3) # возвращаем сумму с округлением до 3 знака после запятой


print(task())
