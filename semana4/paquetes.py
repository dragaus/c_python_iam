import click

@click.command
@click.option("--count", default=1, help="numero de saludos")
def funcion(count):
    print(f"hola {count}")

funcion()