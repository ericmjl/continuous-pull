import click
import subprocess
from time import sleep
import logging
import os


@click.command()
@click.option(
    "--branch",
    "-b",
    default="master",
    type=str,
    help="Branch to pull. Defaults to 'master'.",
)
@click.option(
    "--interval",
    "-i",
    help="Interval between git pulls.",
    default=60,
    type=int,
)
@click.option(
    "--hide/--no-hide",
    "-h/-nh",
    help="Whether or not to hide the output from the tool.",
    default=False,
)
def main(branch: str = "master", interval: int = 60, hide: bool = False):
    logging.info(f"Currently in directory {os.getcwd()}.")
    logging.info(f"Checking out {branch}...")
    subprocess.run(f"git checkout {branch}".split(), capture_output=hide)
    while True:
        subprocess.run("git pull".split(), capture_output=hide)
        sleep(interval)


if __name__ == "__main__":
    main()
