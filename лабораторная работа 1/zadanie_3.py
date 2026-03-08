list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2

first_team = list_players[:middle_index] #срез от начала списка до элемента с индексом середины (оля) не включая его
second_team = list_players[middle_index:] #срез от индекса середины (оля) до конца списка

print(first_team)
print(second_team)
