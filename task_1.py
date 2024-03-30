f = open('astronaut_time.csv', encoding='utf-8').readlines()[1:]
#открываем исходный файл
f_out = open('new_time.txt', 'w', encoding='utf-8')
#открываем файл на запись
f1 = [i.strip().split(',') for i in f]
#создаем список с данными о станциях
for i in f1:
    t1 = i[-1]
    t2 = i[-2].split(':')
    if int(t2[0]) + int(t1) >= 24:
        r = str(int(t1) + int(t2[0]) - 24)
        if len(r) == 1:
            r = '0' + r
    else:
        r = str(int(t1) + int(t2[0]))
        if len(r) == 1:
            r = '0' + r
    #считаем итоговое время
    res_t = [r] + t2[1:]
    f_out.write(''.join(['На станции ', str(i[1]), ' в каюте ',str(i[2]), ' восстановлено время. Актуальное время: ', ':'.join(res_t)]) + '\n')
    #аписываем результат в файл

