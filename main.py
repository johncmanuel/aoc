import argparse
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
from lib.aoc import fetch_and_save_input, get_day_path, get_current_aoc_time

TEMPLATE_PATH = Path("lib/template.py")


def make_cmd(year: int, day: int) -> None:
    """Sets up the folder, downloads input, and copies the solution template."""
    try:
        fetch_and_save_input(year, day)
    except Exception as e:
        print(f"Warning: Could not fetch input ({e}). Creating folder anyway.")
        get_day_path(year, day).mkdir(parents=True, exist_ok=True)

    folder = get_day_path(year, day)
    soln_file = folder / "soln.py"

    if soln_file.exists():
        print(f"Solution file already exists at {soln_file}. Skipping template copy.")
        return

    if TEMPLATE_PATH.exists():
        soln_file.write_text(TEMPLATE_PATH.read_text())
        print(f"Created {soln_file} from template.")
    else:
        soln_file.touch()
        print(f"Created empty file at {soln_file} (Template not found).")


def run_cmd(year: int, day: int) -> None:
    """Dynamically imports and executes the solution file."""
    folder = get_day_path(year, day)
    soln_file = folder / "soln.py"

    if not soln_file.exists():
        raise FileNotFoundError(f"No solution file found at: {soln_file}")

    print(f"Running solution for {year} Day {day}...")

    spec = spec_from_file_location(str(day), soln_file)

    # Solves type error with spec.loader
    if not spec or not spec.loader:
        raise ImportError(f"Could not load spec for {soln_file}")

    module = module_from_spec(spec)
    spec.loader.exec_module(module)


def main():
    now = get_current_aoc_time()

    parser = argparse.ArgumentParser(description="AoC CLI tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_date_args(p):
        p.add_argument(
            "-y",
            "--year",
            type=int,
            default=now.year,
            help=f"Year (default: {now.year})",
        )
        p.add_argument(
            "-d", "--day", type=int, default=now.day, help=f"Day (default: {now.day})"
        )

    make_parser = subparsers.add_parser(
        "make", help="Setup environment for specific day"
    )
    add_date_args(make_parser)

    run_parser = subparsers.add_parser("run", help="Run solution for specific day")
    add_date_args(run_parser)

    args = parser.parse_args()

    try:
        if args.command == "make":
            make_cmd(args.year, args.day)
        elif args.command == "run":
            run_cmd(args.year, args.day)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
