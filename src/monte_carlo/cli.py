"""Console script for monte_carlo."""

import typer
from rich.console import Console

from monte_carlo import utils

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Console script for monte_carlo."""
    console.print("Replace this message by putting your code into monte_carlo.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
