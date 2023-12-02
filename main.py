from lib.aoc import *
import argparse
import subprocess

def make_cmd(url: str, year: str, day: str):
    url = get_current_aoc_url(url, year, day)
    valid_day = validate_day(day)

    create_directory(year, valid_day)
    data = get_input(url)
    create_input_file(data, year, valid_day)

    copy_template(get_folder(year, valid_day))

def run_cmd(year: str, day: str, file: str):
    day = validate_day(day)
    cwd = f"{os.path.dirname(os.path.realpath(__file__))}/"
    subprocess.run(["python", f"{get_folder(year, day)}/{file}.py"], cwd=cwd)

def main():
    parser = argparse.ArgumentParser(description="AoC CLI tools")
    subparsers = parser.add_subparsers(title="commands", dest="command")

    make_parser = subparsers.add_parser("make", help="Sets up environment for current day")
    make_parser.add_argument("--day", type=int, required=True, help="Specify the day (ex. 1, 2, 3, etc)")

    run_parser = subparsers.add_parser("run", help="Run solution")
    run_parser.add_argument("--day", type=int, required=True, help="Specify the day (ex. 1, 2, 3, etc)")
    run_parser.add_argument("--file", type=str, required=True, help="Name of the solution file")

    args = parser.parse_args()

    day = str(args.day)
    year = str(CURRENT_DATE.year)

    if args.command == "make":
        make_cmd(AOC_URL, year, day)
    elif args.command == "run":
        run_cmd(year, day, args.file)
    else:
        raise Exception("Invalid command.")

if __name__ == "__main__":
    main()

# year, day = 2023, "3"
# x = get_current_url(AOC_URL, "9")
# y = save_input(x, year, day)
# print(x)

