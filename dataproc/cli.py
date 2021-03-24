"""Console script for dataproc."""
import typer
from pathlib import Path
from typing import Optional
from dataproc.dataproc import unzip_files


app = typer.Typer()


@app.command()
def unzip(
    in_dir: Path = typer.Argument(
        ..., help="The directory containing the input form files"
    ),
    out_dir: Optional[Path] = typer.Option(
        None,
        "--out_dir",
        help="The directory where the output flat files will be created. Defaults to the current working directory",
    ),
) -> None:
    unzip_files(in_dir, out_dir)

