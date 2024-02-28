import random, argparse, urllib.request, cowsay


def bullscows(guess: str, secret: str) -> (int, int):
    '''
        Возвращает количество "быков" и "коров" из guess в secret
    '''    
    bulls, cows = 0, 0

    for i, j in zip(guess, secret):
        if i == j:
            bulls += 1
        elif i in secret:
            cows += 1

    return bulls, cows


def ask(prompt: str, valid: list[str] = None) -> str:
    '''
        Спрашивает слово у пользователя
    '''
    a = input(cowsay.cowsay(prompt, cow = cowsay.get_random_cow()) + '\n')

    if valid:
        while a not in valid:
            a = input(cowsay.cowsay(prompt, cow = cowsay.get_random_cow()) + '\n')

    return a


def inform(format_string: str, bulls: int, cows: int) -> None:
    '''
        Выводит результат пользователю
    '''
    print(cowsay.cowsay(format_string.format(bulls, cows), cow = cowsay.get_random_cow()))


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    '''
        Обеспечивает геймплей игры "Быки и коровы"
    '''
    secret = random.choice(words)
    tries = 0

    while True:
        
        guess = ask("Введите слово: ", words)
        tries += 1
        b, c = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", b, c)
        if b == len(guess):
            break

    return tries


parser = argparse.ArgumentParser()
parser.add_argument('dictionary', type = str, help = 'dictionary for game as file or URL')
parser.add_argument('length', nargs = '?', default = 5, type = int, help = 'length of secret word')
args = parser.parse_args()

words = []

if args.dictionary[:4] == 'http':
    with urllib.request.urlopen(args.dictionary) as f:
        words = f.read().decode('utf-8').splitlines()
else:
    with open(args.dictionary) as f:
        words = f.read().splitlines()

words = [i for i in words if len(i) == args.length] 

print(gameplay(ask, inform, words))
