


def zamiana(a, b): # a - liczba ktora chce zamienic, b- na jaki system chce ja zamienic
    kon = []
    while a != 0:
        kon.append(a%b)
        a = int(a/b)
    kon = kon[::-1]
    return "".join(str(i) for i in kon)



def odmiana(a, b):
    a = str(a)
    lst = [int(i) for i in a]
    wynik = 0
    k = 0
    lst = lst[::-1]
    for i in range(len(lst)):
        wynik += lst[i]*(b**k)
        k += 1
    return wynik


if __name__ == "__main__":
    print(zamiana(124534, 7))
    print(odmiana(1026034, 7))