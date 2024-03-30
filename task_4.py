f = open('astronaut_time.csv', encoding='utf-8').readlines()[1:]
#открываем исходный файл
f_out = open('station_max_downtime.csv', 'w', encoding='utf-8')
#открываем итоговый файл на запись
f1 = [i.strip().split(',') for i in f]
res = [[i[1],i[-1]] for i in f1 if i[-1] == '9']
#сохраняем данные из исходного файла в список
res_arr = []
d = {}
#создаем словарь
for i in f1:
    if i[1] not in d.keys():
        d[i[1]] = [int(i[-1])]
    else:
        d[i[1]].append(int(i[-1]))
#группируем данные по номеру станции
for i in d.keys():
    d[i] = sum(d[i])
    #считаем общее время простоя
    if d[i] == 9:
        res_arr.append([i,'9'])
        #добавляем в итоговый список номер станции
print(res_arr)
#выводим получившийся список
for i in res_arr:
    f_out.write(' '.join(i) + '\n')
    #записываме результат в итоговый файл
