
def g(strr):
    i = 0
    new_str = ""
    while i < len(strr) - 1:
        new_str = new_str + strr[i+1]
        i = i+1
    return new_str


def f(str):
    if len(str) == 0:
        return ""
    elif len(str) == 1:
        return str
    else:
        return f(g(str))+ str[0]

    return

def h (n,str):
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n +1

        str = f(str)
    return str

def pow(x, y):
    if y == 0:
        return 1
    else:
        return x + pow(x, y-1)

    return

print(h(1,"fruits"))
print(h(2,"fruits"))
print(h(2,"fruits"))
print(h(pow(2, 1000000000000000),"fruits"))
print(h(pow(2, 9831050005000007),"fruits"))




