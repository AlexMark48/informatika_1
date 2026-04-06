import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as file_input: # открываем файл для чтения
        # списку присваиваем элементы - словари для каждой строчки файла методом DictReader
        spisok = [stroka for stroka in csv.DictReader(file_input)]

    with open(OUTPUT_FILENAME, "w") as file: # открываем/создаем файл для записи
        json.dump(spisok, file, indent = 4) # сериализуем данные в формат json с отступом 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
