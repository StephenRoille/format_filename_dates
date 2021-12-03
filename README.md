# Format Filename Dates

This library allows to batch-rename files by converting the format of dates they start with.

## Example Usage
```bash
# specify the source directory
python -m format_filename_dates --src="./path/to/files"

# specify the pathname pattern expansion
# visit https://docs.python.org/3/library/glob.html?highlight=glob#module-glob
python -m format_filename_dates --src="./path/to/files" --regex="*."

# specify the input and output date formats
# visit https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
python -m format_filename_dates --src=./path/to/files --date-format-in="%y%m%d" --date-format-in="%Y%m%d"

# use colored output
python -m format_filename_dates --src=./path/to/files --color

# display summary without renaming files
python -m format_filename_dates --src=./path/to/files --dry-run

# specify the separator between the date and the rest of the file name
python -m format_filename_dates --src=./path/to/files --separator="_"
```


## Complete Command Line Usage

```bash
usage: __init__.py [-h] [--src [SRC]] [--regex [REGEX]]
                   [--date-format-in [DATE_FORMAT_IN]]
                   [--date-format-out [DATE_FORMAT_OUT]]
                   [--separator [SEPARATOR]] [--dry-run]

File names date converter

optional arguments:
  -h, --help            show this help message and exit
  --src [SRC]           Source directory containing files to rename
  --regex [REGEX]       Name pattern matching to include files [default: *]
  --date-format-in [DATE_FORMAT_IN]
                        Input date pattern
                        (https://docs.python.org/3/library/datetime.html)
  --date-format-out [DATE_FORMAT_OUT]
                        Output date pattern
                        (https://docs.python.org/3/library/datetime.html)
  --separator [SEPARATOR]
                        Date separator [default: _]
  --dry-run             Show old and new names without renaming them
  -h, --help            show this help message and exit
  --src [SRC]           Source directory containing files to rename
  --regex [REGEX]       Name pattern matching to include files
  --date-format-in [DATE_FORMAT_IN]
                        Inuput date pattern
  --date-format-out [DATE_FORMAT_OUT]
                        Output date pattern
  --separator [SEPARATOR]
                        Date separator
  --dry-run             Show old and new names without renaming them
```

## Dependencies

None! This package only relies on the Python standard library.


## License

This project can be used under the MIT license.
