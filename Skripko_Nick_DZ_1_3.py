# Склонение слова

word: str = 'Процент'
for n in range(1, 101, 1):
    if (n % 10 == 0
        or n == 11
        or n == 12
        or n == 13
        or n == 14
        or 5 <= n % 10 <= 9):
        print(n, word + 'ов')
    elif n % 10 == 1:
        print(n, word)
    elif 2 <= n % 10 <= 4:
        print(n, word + 'а')


