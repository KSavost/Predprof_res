
f = open('astronaut_time.csv', encoding='utf-8').readlines()[1:]
#открываем исходный файл
f1 = [i.strip().split(',') for i in f]
#создаем список с данными о станциях
d = {}
#словарь с группами станций
d1 = {}
#словарь с номерами кают
d_res = {}
#итоговй словарь(хэш таблица)
for i in f1:
    group = i[1].split('-')[0]
    #получаем номер группы
    if group in d.keys():
        d[group].append(int(i[-1]))
        d1[group].append(i[2])
    else:
        d[group] = [int(i[-1])]
        d1[group] = [i[2]]
    #добавляем значения в словари по общей группе станций
for i in d.keys():
    d_res[i] = [', '.join(d1[i]),str(sum(d[i])/len(d[i]))]
    #записываем полную информацию в результирующеую хеш таблицу
for i in d_res.keys():
    cabins = ', '.join(d_res[i][:-1])
    print(f'Номер группы: {i}, Каюты: {cabins}. Время простоя: {d_res[i][-1]}')
    #выводим хеш таблицу
