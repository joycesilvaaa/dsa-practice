def soma(a, b):
    return a + b

def menos(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def result(a, b):
    print(soma(a=a, b=b))
    print(menos(a=a, b=b))
    print(multiplicacao(a=a, b=b))

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    result(a, b)