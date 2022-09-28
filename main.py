sec = int(input('Секунди -  '))
ver = int(input(' 1 часи \n 2 мінути \n 3 секунди \n'))
if ver == 1:
    r = int(sec/60/60)
    hours = int(24-r)
    p = 'часи'
    y = p
    print("До півночі залишилось ",hours,"часів")
elif ver == 2:
    r = int(sec/60)
    mins = int(1440-r)
    k = 'мінути'
    y = k
    print("До півночі залишилось ",mins,"хвилин")
elif ver == 3:
    r = int(86400-sec)
    sec_2 = r
    n = 'секунди'
    y = n
    print("До півночі залишилось ",sec_2,"секунд")
else:
    end = 86400
    between = end - sec
    min = 0
    h = 0
    print(f'Ваш час: {int(sec/3600)}:{int((sec%3600)/60)}:{int((sec%3600)%60)}')
    if between>0:
        h = int(between/3600)
        min = int((between%3600)/60)
        sec = int((between%3600)%60)
        print(f'До півночі залишилось: {h}:{min}:{sec}')
    m = 'все число'
    y = m


