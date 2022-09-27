diametr = int(input("Введіть діаметр кола - "))
pi = float(3.14)
ver = int(input(' 1 площа \n 2 периметр \n'))
if ver == 1:
    S = pi/4*diametr*diametr
    p = 'площа'
    y = p
    print("Площа кола", S)
elif ver == 2:
    r = float(diametr/2)
    P = float(2*pi*r)
    k = 'периметр'
    y = k
    print("Периметр кола", P)