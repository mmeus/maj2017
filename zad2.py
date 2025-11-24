#zad2.2
licznik = 0
def licz(x):
    global licznik
    licznik += 1
    if x == 1:
        return 1
    else:
        w = licz(x // 2)
        if x % 2 == 1:
            return w + 1
        else:
            return w - 1

for x in range(1, 1000):
    licznik = 0
    licz(x)
    print(x, licznik)
#odp: B) x = 2^k-1

#zad2.3
for x in range(101, 1000000):
    if licz(x) == 0:
        print(x)
        break