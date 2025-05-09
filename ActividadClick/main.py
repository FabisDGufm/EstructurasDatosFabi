import click
from datetime import datetime
import random

@click.group()
def cli():
    pass

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")

@cli.command()
def timenow():
    print(f'\n{datetime.now()}\n')

@click.command()
def suerte():
    print(f'Tu numero de la suerte de hoy es: ' + (str(random.randint(0,10))))

@click.command()
def decidir():
    des = random.randint(0,2)
    if (des == 0):
        print(f'No, no lo hagas bro')
    elif (des == 1):
        print(f'No me preguntes a mi, ni idea, suerte')
    else:
        print(f'Sip, dale, sin miedo')
    

if __name__ == '__main__':
    decidir()

