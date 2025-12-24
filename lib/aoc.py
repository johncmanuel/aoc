import os
from datetime import datetime
from pathlib import Path
from typing import List, Union

import pytz
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://adventofcode.com"
BASE_SOLN_DIR = Path("solns")
EASTERN_TZ = pytz.timezone("America/New_York")


def _get_session() -> str:
    """Retrieves the AoC session token."""
    if not (session := os.getenv("session")):
        raise EnvironmentError("Environment variable 'session' is missing.")
    return session


def _format_date(year: Union[int, str], day: Union[int, str]) -> tuple[str, str]:
    """Validates and formats year and day (e.g., 1 -> '01')."""
    day_int = int(day)
    if not (1 <= day_int <= 25):
        raise ValueError(f"Day must be between 1 and 25. Got: {day}")
    return str(year), f"{day_int:02d}"


def get_current_aoc_time() -> datetime:
    """Returns the current time in AoC's timezone (EST/EDT)."""
    return datetime.now(EASTERN_TZ)


def get_day_path(year: Union[int, str], day: Union[int, str]) -> Path:
    """Returns the local directory path: solns/YYYY/dayDD."""
    y_str, d_str = _format_date(year, day)
    return BASE_SOLN_DIR / y_str / f"day{d_str}"


def fetch_and_save_input(year: Union[int, str], day: Union[int, str]) -> Path:
    """
    Creates the directory structure, fetches input from AoC,
    saves it to input.txt, and returns the file path.

    """
    # y_str, d_str = _format_date(year, day)
    folder = get_day_path(year, day)
    folder.mkdir(parents=True, exist_ok=True)

    file_path = folder / "input.txt"

    # Only fetch if we don't already have it
    if not file_path.exists():
        url = f"{BASE_URL}/{year}/day/{int(day)}/input"
        resp = requests.get(url, cookies={"session": _get_session()})
        resp.raise_for_status()

        file_path.write_text(resp.text)
        print(f"Downloaded input to {file_path}")

    return file_path


def extract_input(year: Union[int, str], day: Union[int, str]) -> List[str]:
    """Reads input.txt for a specific day and returns a list of lines."""
    file_path = get_day_path(year, day) / "input.txt"

    if not file_path.exists():
        fetch_and_save_input(year, day)

    return file_path.read_text().splitlines()
