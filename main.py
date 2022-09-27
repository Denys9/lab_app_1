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
    r = int(sec / 60 / 60)
    hours = int(24 - r)
    r = sec / 60
    mins = 1440 - r
    r = 86400 - sec
    sec_2 = r
    m = 'все число'
    y = m
    print("До півночі залишилось ",hours,":",mins,":",sec_2,": секунд")


