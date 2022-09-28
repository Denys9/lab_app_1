hours = int(input('Введіть кількість годин - '))
if hours>=0 or 24 and hours<6:
    print('Good night!')
elif hours>=6 and hours<13:
    print('Good Morning!')
elif hours>=13 and hours<17:
    print('Good day!')
elif hours>=17 and hours<23:
    print('Good Evening!')