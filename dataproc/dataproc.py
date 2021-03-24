"""Main module."""
import os
import tempfile
import zipfile
from pathlib import Path


def unzip_files(in_dir: Path, out_dir: Path) -> None:
    """
    :param out_dir:
    :param in_dir:
    :return:
    """
    for zip_file in in_dir.glob("*.zip"):
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(out_dir)
