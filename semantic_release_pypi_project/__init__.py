def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def abs(a):
    if a < 0:
        return a*(-1)
    return a

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

if __name__ == '__main__':
    print(f'1+1={add(1,1)}')
    print(f'2-1={sub(2,1)}')
