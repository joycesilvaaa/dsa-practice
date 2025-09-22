# pode ser dividido por 4
# se o ano for dividido por 100, ele não é bissexto, a menos que seja também divisível por 400

def is_leap(year):
    if year % 4 == 0:
        return True if year % 100 != 0 or year % 400 == 0 else False
    return False


print(is_leap(2000))  # True
print(is_leap(1900))  # False
print(is_leap(2020))  # True
print(is_leap(1992))  # True