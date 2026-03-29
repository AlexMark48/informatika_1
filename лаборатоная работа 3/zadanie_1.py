def index_ (list, item): # функция с 2 аргументами: общий список и изучаемый элемент
    if item in list: # проверяем есть ли нужный элемент в общем списке
        return list.index(item) # если есть возвращаем его индекс из общего списка
    else :
        return None # если нет возвращаем значение ничего


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index_(items_list, find_item) # вызов функции с 2 аргументами: общий список и изучаемый элемент
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
