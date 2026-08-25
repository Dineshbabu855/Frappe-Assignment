import click


@click.command()
def siu():
    click.echo("Hello from the custom Bench CLI!")


@click.command("hello-app")
def hello_app():
    click.echo("Hello from custom command!")


commands = [siu, hello_app]