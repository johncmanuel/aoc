""" Python library for interacting with AoC """

import pytz
from datetime import datetime
import requests
import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()


def get_env_var(env_var) -> str:
    var = os.getenv(env_var)
    if not var:
        raise Exception(f"Environment variable {env_var} not set")
    return var


AOC_URL = "https://adventofcode.com"
# AOC uses Eastern time zone
EASTERN_TZ_US = pytz.timezone("America/New_York")
CURRENT_DATE = datetime.now(EASTERN_TZ_US)


def validate_day(day: str) -> str:
    # if day < "0" or day > "32":
    #     raise Exception("Invalid day")
    day_int = int(day)
    if 0 < day_int < 10:
        day = f"0{day}"
    if day_int > 32 or day_int < 1:
        raise Exception("Invalid day")
    return day


# Example URL: https://adventofcode.com/2020/day/1
def get_current_aoc_url(year: str, day: str) -> str:
    return f"{AOC_URL}/{year}/day/{day}"


# Example directory structure: solns/2020/day01
def create_directory(year: str, day: str) -> None:
    f = get_folder_name(year, day)
    sub_dir = Path(f)
    sub_dir.mkdir(parents=True, exist_ok=True)


def get_folder_name(year: str, day: str) -> str:
    return f"solns/{year}/day{day}"


def get_input(url: str) -> str:
    sess = get_env_var("session")
    return requests.get(f"{url}/input", cookies={"session": sess}).text


def create_input_file(data: str, year: str, day: str) -> None:
    f = get_folder_name(year, day)
    data_file = f"{f}/input.txt"
    with open(data_file, "w") as f:
        f.write(data)


def extract_input(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.rstrip() for line in f]
