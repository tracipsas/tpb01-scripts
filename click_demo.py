import click
import time
import datetime

@click.command()
@click.option(
    "--increment",
    default=1,
    help="Taille de l'incrément"
)
@click.argument(
    "INTERVAL",
    type=int
)
def counter(increment, interval):
    count = 0
    while True:
        print("[{}] {}".format(
            datetime.datetime.now().strftime("%H:%M:%S"), count
        ))
        count += increment
        time.sleep(interval)

if __name__ == "__main__":
    counter()
