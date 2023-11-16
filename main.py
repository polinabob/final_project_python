import click
from kitchen import *


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza_name', nargs=1)
@click.argument('size', default='L', nargs=1)
def order(pizza_name: str, size: str, delivery: bool):
    """Bakes and delivers pizza."""

    if pizza_name not in PIZZA_OPTIONS:
        print('There is no such pizza on the menu ˙◠˙')
        return 0
    if size not in ('L', 'XL'):
        print('Invalid size ˙◠˙')
        return 0

    pizza = Pizza(name=pizza_name, size=size)
    pizza.bake()
    if delivery:
        pizza.delivery()
    print('Enjoy your pizza! ˶ᵔ ᵕ ᵔ˶')


@cli.command()
def menu():
    """Prints menu."""

    emojis = {'margherita': '🍕', 'pepperoni': '🍖', 'hawaiian': '🍍'}
    for pizza in PIZZA_OPTIONS:
        print(f'- {pizza.capitalize()} {emojis[pizza]}:',
              ', '.join(PIZZA_OPTIONS[pizza])+'.')


if __name__ == '__main__':
    cli()

