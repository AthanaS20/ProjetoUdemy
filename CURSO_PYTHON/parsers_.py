from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    '-b', '--basic',
    help='Mostra, "Olá, mundo!" na tela',
    type=str,
    metavar='STRING',
    default='Olá, mundo',
    required=False
                    
)

args = parser.parse_args()

if args.basic is None:
    ('Você não passou nenhum argumento.')
else:
    (f'O valor de b: {args.basic}')