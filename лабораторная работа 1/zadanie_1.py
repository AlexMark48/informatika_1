numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

nomer_propuska = numbers.index(None) # находим индекс пропущенного элемента в списке с помощью команды .index
number_new = numbers[:nomer_propuska] + numbers[nomer_propuska + 1::] # список из всех элементов кроме пропущенного
numbers[4] = round((sum(number_new) / (len(number_new) + 1)), 2) #замена пропуска из изначального списка

print("Измененный список:", numbers)
