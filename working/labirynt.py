from collections import deque

def openfile(path):
    with open(path) as file:
        lst = [list(line.strip()) for line in file]
    return lst

def bfs(labirynt,pocz,kon):
    kierunki = [(-1,0), (1,0),(0,-1),(0,1)]
    q = deque([pocz])
    odwiedzony = set()
    odwiedzony.add(pocz)
    parent = {pocz: None}
    while q:
        u = q.popleft()
        if u == kon:
            path =[]
            while u:
                path.append(u)
                u = parent[u]
            return path[::-1]
        for directions in kierunki:
            sasiad = (directions[0]+u[0],u[1] + directions[1])
            if (0 <= sasiad[0] < len(labirynt)) and (0<=sasiad[1]< len(labirynt[0])) and labirynt[sasiad[0]][sasiad[1]] != "#" and sasiad not in odwiedzony:
                odwiedzony.add(sasiad)
                parent[sasiad] = u
                q.append(sasiad)
    return None

def znajdzpoczikon(labirynt):
    for i in range(len(labirynt)):
        for j in range(len(labirynt[i])):
            if labirynt[i][j] == "S":
                pocz = (i,j)
            elif labirynt[i][j] == "W":
                kon = (i,j)
    return pocz, kon

if __name__ == "__main__":
    labirynt = openfile("D:\Projects\programiki\labirynt.txt")
    pocz, kon = znajdzpoczikon(labirynt)
    print(bfs(labirynt,pocz,kon))