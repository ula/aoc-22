import asyncio
import click
from typing import Any, Optional
import importlib

from aoc22.utils import get_base


@click.command()
@click.argument("day", type=int)
@click.argument("args", nargs=-1)
@click.option("--input", "-i", "input_file")
def main(day: int, args: Optional[Any] = None, input_file: Optional[str] = None):
    day_dir = f"0{day}" if day < 10 else str(day)
    mod = importlib.import_module(f"aoc22.{day_dir}")
    input_file = input_file or f"{get_base()}/{day_dir}/input.txt"
    try:
        click.echo(f"Running day {day}...")
        result = asyncio.run(getattr(mod, "main")(*args, f=input_file))
        click.echo(f"Result: {result}")
    except (TypeError, FileNotFoundError) as e:
        raise
        # raise click.UsageError(str(e)) from e
    else:
        click.echo("Done!")
