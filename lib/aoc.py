""" Python library for interacting with AoC """

from datetime import datetime
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
import shutil


load_dotenv()

AOC_URL = "https://adventofcode.com"
CURRENT_DATE = datetime.now()

def validate_day(day: str) -> str:
    if day < "0" or day > "32":
        raise Exception("Invalid day")
    if day > "0" and day <= "9":
        day = f"0{day}"
    return day

def get_current_aoc_url(url: str, year: str, day: str) -> str:
    return f"{url}/{year}/day/{day}"

def create_directory(year: str, day: str) -> None:
    sub_dir = Path(f"{year}/day{day}")
    sub_dir.mkdir(parents=True, exist_ok=True)

def get_folder(year: str, day: str) -> str:
    return f"{year}/day{day}"

def get_input(url: str):
    return requests.get(f"{url}/input", cookies={"session": os.getenv("session")}).text

def create_input_file(data: str, year: str, day: str, filename: str = "input"):
    with open(f"{get_folder(year, day)}/{filename}.txt", "w") as f:
        f.write(data)

def copy_template(dst: str) -> None:
    shutil.copy("./lib/template.py", dst)

def extract_input(filename: str) -> list:
    with open(filename) as f:
        return [line.rstrip() for line in f]
