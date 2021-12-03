"""This library allows to batch-rename files by converting the format of dates they start with.
"""
import argparse
import pathlib
from types import SimpleNamespace

__version__ = "0.1.0"


def parse_args() -> SimpleNamespace:
    parser = argparse.ArgumentParser(description="File names date converter")
    parser.add_argument(
        "--src",
        type=pathlib.Path,
        nargs="?",
        help="Source directory containing files to rename",
        required=True,
    )
    parser.add_argument(
        "--date-format-in",
        type=str,
        nargs="?",
        default="%y%m%d",
        help="Input date pattern (https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)",
    )
    parser.add_argument(
        "--date-format-out",
        type=str,
        nargs="?",
        default="%Y%m%d",
        help="Output date pattern (https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)",
    )
    parser.add_argument(
        "--regex",
        type=str,
        nargs="?",
        default="*",
        help="Name pattern matching to include files [default: *]",
    )

    parser.add_argument(
        "--separator",
        type=str,
        nargs="?",
        default="_",
        help="Date separator [default: _]",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show old and new names without renaming them",
    )
    parser.add_argument("--color", action="store_true", help="Use colored output")

    args = parser.parse_args()

    filepath = pathlib.Path(args.src).resolve()
    if not filepath.is_dir():
        raise NotADirectoryError(
            f"'{filepath}' does not exist or is not a valid directory."
        )
    return args
