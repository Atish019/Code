"""Console script for zomato_top3_recco."""
import zomato_top3_recco

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for zomato_top3_recco."""
    console.print("Replace this message by putting your code into "
               "zomato_top3_recco.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
