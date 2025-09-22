
def check_number(n):
    if n % 2 != 0: 
        return "Weird"
    elif n % 2 == 0:
        if (2 <= n <= 5) or (n > 20):
            return "Not Weird"
        elif (6 <= n <= 20):
            return "Weird"


if __name__ == '__main__':
    n = int(input().strip())
    print(check_number(n))
