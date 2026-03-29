def find_common_participants (group1, group2, rasdelitel = ","): # функция принимает 2 строки и разделитель
    guis1 = set(group1.split(rasdelitel)) # создаем коллекцию из элементов 1 строки (имён) разделенных данным знаком
    guis2 = group2.split(rasdelitel) # создаем список из элементов 2 строки (имён)  разделенных данным знаком
    vmeste = guis1.intersection(guis2) # создаем новую коллекцию, в которой находятся общие элементы из 1 и 2
    return list(vmeste) # возвращаем полученную коллекцию в в иде списка


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print (find_common_participants(participants_first_group, participants_second_group, "|")) # выводим итоговый список
