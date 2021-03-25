"""Main module."""
import os
import tempfile
import zipfile
import typer
from pathlib import Path


def unzip_files(in_dir: Path, out_dir: Path) -> None:
    """
    :param out_dir:
    :param in_dir:
    :return:
    """
    for zip_file in in_dir.glob("*.zip"):
        typer.secho(f"Unzipping: {zip_file.name}", bg=typer.colors.BLACK, fg=typer.colors.BRIGHT_YELLOW)
        try:
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(out_dir)
        except Exception as e:
            typer.secho("failed!", bg=typer.colors.BLACK, fg=typer.colors.BRIGHT_MAGENTA)
