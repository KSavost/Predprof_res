f = open('astronaut_time.csv', encoding='utf-8').readlines()[1:]
#открываем исходный файл
print('Пожалуйства, введите номер интересующей вас станции.')
number_station = input()
#ввод номера станции
f1 = [i.strip().split(',') for i in f]
#список всех станций с информацими о них
d = {}
#словарь с ключами кают в виде их номера
while number_station != 'stop':
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
        res_t = [r] + t2[1:]
        #подсчет актуального времени
        d[i[1]] = ''.join(['На станции ', str(i[1]), ' в каюте ', str(i[2]), ' восстановлено время. Актуальное время: ', ':'.join(res_t)]) + '\n'
        #запись информации о станции в словарь
    if number_station in d.keys():
        print(d[number_station])
        #вывод информации о станции в случае проблем у таковой
    else:
        print('На этой станции все хорошо')
    print('Пожалуйства, введите номер интересующей вас станции.')
    number_station = input()
    #ввод


