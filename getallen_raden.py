import random

print('raad het getal vanaf 0 tot en met 20')

n=random.randint(1,20)
g=0

while(g!=n):
    g=input('raad het getal ')
    g=int(g)
    if(g>n):
        print('te hoog')
    if(g<n):
        print('te laag')
print('goed geraden')

a = 'on'

while a == 'on':

    print('raad het getal vanaf 0 tot en met 20')

    n = random.randint(1, 20)
    g = 0

    while (g != n):
        g = input('raad het getal ')
        g = int(g)
        if (g > n):
            print('te hoog')
        if (g < n):
            print('te laag')
    print('goed geraden :)')
    print('* je hebt gewonnen *')
    print('nieuw potje start automatisch')