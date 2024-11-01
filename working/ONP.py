class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.insert(0, item)
    def __str__(self):
        return str(self.items)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def isnotempty(self):
        return self.items != []

def onp():
    s = Stack()
    operation = input()
    lst = operation.split(" ")
    lst2 = []

    for item in lst:
        try:
            lst2.append(int(item))
        except ValueError:
            lst2.append(item)


    for i in range(len(lst2)):
        if isinstance(lst2[i], int):
            s.push(lst2[i])
        else:
            v2 = s.pop()
            v1 = s.pop()
            match lst2[i]:
                case '+': result = v1 + v2
                case '-': result = v1 - v2
                case '*': result = v1 * v2
                case '/': result = v1 / v2
            s.push(result)

    print(s.peek()) 

if __name__ ==  "__main__":
    onp()