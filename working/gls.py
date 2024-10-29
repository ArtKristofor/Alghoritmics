import random
def LCG(a,p,m):
    x0 = 0
    x = x0
    losowe = []
    while True:
        x = (a*x+p) % m
        losowe.append(x)
        if x == x0:
            break
    print(losowe)
    print(random.choice(losowe))
if __name__ == "__main__":
    LCG(13,7,12)