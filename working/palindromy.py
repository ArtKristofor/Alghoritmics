import random

def palindromy1():
    dl = int(input("podaj długosc łancucha: "))
    lancuch = ""
    for i in range(dl):
        lancuch += chr(random.randrange(65,69))
    print(lancuch)
    for i in range(dl):
        for j in range(i + 1, dl + 1):
            substring = lancuch[i:j]
            if substring == substring[::-1]:  
                if len(substring) >= 2:
                    print(substring)

def palindromy2():
    lancuch = str(input())
    dl = len(lancuch)
    r = [[0 for j in range(dl+1)] for i in range(2)]
    print(r)
    lancuch = "$"+lancuch+"#"
    for i in range(2):
        r[i][0], rp,j=0,0,1
        while j <= dl:
            while lancuch[j-rp-1] == lancuch[i+j+rp]:
                rp += 1
            r[j][i], k = rp, 1
            print(rp)
            while (r[i][j-k] != rp-k) and k < rp:
                r[i][j+k] = min(r[i][j-k], rp-k)
                k+=1
            rp = max(rp-k, 0)
        j += k
    for i in range(1, dl+1):
        for j in range(2):
            for rp in range(r[j][i], 0, -1):
                for k in range(1, i-rp):
                    print(" ", end="")
                print(lancuch[i-rp-1:i-1+rp+j])

if __name__ == "__main__":
    palindromy2()