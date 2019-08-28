import click
import subprocess
from time import sleep
import logging
import os


@click.command()
@click.option(
    "--interval",
    prompt="Interval between git pulls (seconds)",
    help="Interval between git pulls.",
    default=60,
    type=int,
)
@click.option(
    "--hide-output",
    prompt="Do you want to hide output?",
    help="Whether or not to hide the output from the tool.",
    type=bool,
    default=False,
)
def main(interval: int = 60, hide_output: bool = False):
    logging.info(f"Currently in directory {os.getcwd()}.")
    while True:
        subprocess.run("git pull", capture_output=hide_output, shell=True)
        sleep(interval)


if __name__ == "__main__":
    main()
