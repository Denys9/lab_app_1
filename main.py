giga = int(input("Введіть розмір файлу у гігабайтах - "))
inetbit = int(input("Введіть швидкість інтернету у бітах в секунду - "))
ver = int(input(' 1 часи \n 2 хвилини \n 3 секунди \n'))
if ver == 1:
    r = giga*8589934592
    t = int(r/inetbit/60/60)
    p = 'часи'
    y = p
    print("В часах це буде - ", t)
elif ver == 2:
    r = giga * 8589934592
    t = int(r / inetbit / 60)
    k = 'хвилини'
    y = k
    print("В хвилинах це буде - ", t)
elif ver == 3:
    r = giga * 8589934592
    t = int(r / inetbit)
    n = 'секунди'
    y = n
    print("В секундах це буде - ",t)