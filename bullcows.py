import random


def bullcows(guess: str, secret: str) -> (int, int):
    
    bulls, cows = 0, 0

    for i, j in zip(guess, secret):
        if i == j:
            bulls += 1
        elif i in secret:
            cows += 1

    return bulls, cows


def ask(prompt: str, valid: list[str] = None) -> str:
    
    a = input(prompt)

    if valid:
        while a not in valid:
            a = input(prompt)

    return a


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    
    secret = random.choice(words)
    tries = 0

    while True:
        
        guess = ask("Введите слово: ", words)
        tries += 1
        b, c = bullcows(guess, secret)
        inform("Быки: {}, Коровы: {}", b, c)
        if b == len(guess):
            break

    return f'Вы победили за {tries} попыток'



