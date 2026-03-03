memory_mbt = 1.44
stranici = 100
strok_v_stranice = 50
simvoli_v_stroke = 25
ves_simvola_bait = 4

memory_bait = memory_mbt * 1024 * 1024 # переводим из мегабайтов в байты память на диске
memory_one_book = stranici * strok_v_stranice * simvoli_v_stroke * ves_simvola_bait
# считаем вес в байтах одной книги
count_book = memory_bait // memory_one_book #считаем какое количество целых книг поместится
print("Количество книг, помещающихся на дискету:", int(count_book)) # используем int чтобы ответ был целым
