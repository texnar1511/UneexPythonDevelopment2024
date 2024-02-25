import argparse, cowsay

parser = argparse.ArgumentParser()
parser.add_argument('message', nargs = '?', type = str, help = 'cow saying message')
parser.add_argument('-l', action = 'store_true', help = 'print cows list')
parser.add_argument('-e', type = str, help = 'eyes string')
parser.add_argument('-T', type = str, help = 'tongue string')
parser.add_argument('-f', type = str, help = 'cowfile')
parser.add_argument('-W', type = int, help = 'message width (actually width will be one less)')
parser.add_argument('-b', action = 'store_true', help = 'borg mode')
parser.add_argument('-d', action = 'store_true', help = 'dead mode')
parser.add_argument('-g', action = 'store_true', help = 'greedy mode')
parser.add_argument('-p', action = 'store_true', help = 'paranoia mode')
parser.add_argument('-s', action = 'store_true', help = 'thoroughly stoned mode')
parser.add_argument('-t', action = 'store_true', help = 'tired mode')
parser.add_argument('-w', action = 'store_true', help = 'wired mode')
parser.add_argument('-y', action = 'store_true', help = 'youthful appearance mode')

args = parser.parse_args()

if args.l:
    print(cowsay.list_cows())
elif args.message:
    eyes = args.e if args.e else 'oo'
    tongue = args.T if args.T else '  '
    cow = args.f if args.f else 'default'
    width = args.W if args.W else 40
    preset = ''
    for i in 'bdgpstwy':
        preset += i if getattr(args, i) else ''

    print(cowsay.cowsay(args.message, cow, preset, eyes, tongue, width - 1))

