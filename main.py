from lib.aoc import (
    get_current_aoc_url,
    get_input,
    create_directory,
    create_input_file,
    get_folder_name,
    validate_day,
    CURRENT_DATE,
)
import argparse
from importlib.util import spec_from_file_location, module_from_spec
import os
import shutil


def make_cmd(year: str, day: str):
    url = get_current_aoc_url(year, day)
    valid_day = validate_day(day)
    folder = get_folder_name(year, valid_day)

    if os.path.exists(folder):
        raise Exception("Folder already exists:", folder)

    data = get_input(url)
    create_directory(year, valid_day)
    create_input_file(data, year, valid_day)

    shutil.copy("./lib/template.py", folder)
    os.rename(f"{folder}/template.py", f"{folder}/soln.py")


def run_cmd(year: str, day: str):
    """Source for solution: https://stackoverflow.com/a/54956419"""
    day = validate_day(day)
    folder = get_folder_name(year, day)
    soln = f"{folder}/soln.py"

    if not soln:
        raise Exception("No solution file found for day:", day, "year:", year)

    spec = spec_from_file_location(day, soln)
    if not spec:
        raise Exception("Invalid file", soln)

    module = module_from_spec(spec)

    # Solves type error with spec.loader
    if not spec.loader:
        raise ImportError("Spec Loader not found", soln)

    spec.loader.exec_module(module)


def main():
    parser = argparse.ArgumentParser(description="AoC CLI tools")
    subparsers = parser.add_subparsers(title="commands", dest="command")

    # Leave arguments blank if using current year and day
    make_parser = subparsers.add_parser(
        "make", help="Sets up environment for current day"
    )
    make_parser.add_argument(
        "-y",
        type=int,
        required=False,
        help="Specify the year (ex. 2020, 2021, etc)",
    )
    make_parser.add_argument(
        "-d",
        type=int,
        required=False,
        help="Specify the day (ex. 1, 2, 3, etc)",
    )

    run_parser = subparsers.add_parser("run", help="Run solution")
    run_parser.add_argument(
        "--y",
        type=int,
        required=False,
        help="Specify the year (ex. 2020, 2021, etc)",
    )
    run_parser.add_argument(
        "--d",
        type=int,
        required=False,
        help="Specify the day (ex. 1, 2, 3, etc)",
    )
    args = parser.parse_args()

    day = str(CURRENT_DATE.day) if not args.day else str(args.day)
    year = str(CURRENT_DATE.year) if not args.year else str(args.year)

    if args.command == "make":
        make_cmd(year, day)
    elif args.command == "run":
        run_cmd(year, day)
    else:
        raise Exception("Invalid command.")


if __name__ == "__main__":
    main()
