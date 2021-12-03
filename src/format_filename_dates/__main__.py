import datetime
import pathlib
from typing import Iterable
from types import SimpleNamespace

from format_filename_dates import parse_args


def generate_summary(args: SimpleNamespace, files: Iterable[pathlib.Path]) -> dict:
    files_info = {}
    for file in files:
        if not file.is_file():
            continue

        # split filename based on command line separator
        try:
            old_date_str, remainder = file.stem.split(args.separator, maxsplit=1)

        except ValueError:
            raise ValueError(
                f"Could not parse filename '{file.stem}' with separator '{args.separator}'"
            )

        # parse date
        try:
            old_date_obj = datetime.datetime.strptime(old_date_str, args.date_format_in)
            new_date_str = old_date_obj.strftime(args.date_format_out)
            new_name = new_date_str + args.separator + remainder + file.suffix
        except Exception:
            new_date_str = old_date_str
            new_name = file.stem

        rename = old_date_str != new_date_str and not args.dry_run
        if rename:
            file.rename(file.parent / new_name)

        files_info[file.name] = {
            "suffix": file.suffix,
            "dates": {"old": old_date_str, "new": new_date_str},
            "renamed": rename,
        }

    return files_info


def print_summary_to_stdout(args: SimpleNamespace, files_info: dict) -> None:
    class bcolors:
        HEADER = "\033[95m" if args.color else ""
        OKBLUE = "\033[94m" if args.color else ""
        OKGREEN = "\033[92m" if args.color else ""
        WARNING = "\033[93m" if args.color else ""
        FAIL = "\033[91m" if args.color else ""
        ENDC = "\033[0m" if args.color else ""
        BOLD = "\033[1m" if args.color else ""
        UNDERLINE = "\033[4m" if args.color else ""

    for filename, properties in files_info.items():
        print(f"- file: {bcolors.BOLD}{filename}{bcolors.ENDC}")
        if properties["renamed"]:
            print(f"  renamed: {bcolors.OKGREEN}Yes{bcolors.ENDC}")
            print(
                f"  date: {bcolors.WARNING}{properties['dates']['old']}{bcolors.ENDC} -> {bcolors.OKBLUE}{properties['dates']['new']}{bcolors.ENDC}"
            )
        else:
            print(f"  renamed: {bcolors.FAIL}No{bcolors.ENDC}")
            print(
                f"  date: {bcolors.WARNING}{properties['dates']['old']}{bcolors.ENDC} -> {bcolors.WARNING}{properties['dates']['new']}{bcolors.ENDC}"
            )


def main():
    args = parse_args()
    filepaths = pathlib.Path(args.src).resolve().glob(args.regex)
    files_info = generate_summary(args, filepaths)
    print_summary_to_stdout(args, files_info)


if __name__ == "__main__":
    main()
