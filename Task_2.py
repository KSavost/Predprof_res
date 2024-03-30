import time



alist = open('astronaut_time.csv', encoding='utf-8').readlines()[1:]
for i in range(1, len(alist)):
    temp = alist[i]
    j = i - 1
    while (j >= 0 and temp.split(',')[2] > alist[j].split(',')[2]):
        alist[j + 1] = alist[j]
        j = j - 1
    alist[j + 1] = temp
f1 = [i.strip().split(',') for i in alist]
for i in f1[:3]:
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
    print(''.join(['На станции ', str(i[1]), 'в каюте ', str(i[2]), 'восстановлено время. Актуальное время: ',
                   ':'.join(res_t)]) + '\n')