"""Module for testing miscellaneous functions."""
import calendar
from collections import Counter, defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime as dt
import dateutil.tz as dtz
from decimal import Decimal, ROUND_HALF_UP
from getpass import getpass
from json import dumps, loads
from logging import Logger, Formatter, StreamHandler, getLogger, INFO, DEBUG
from math import prod
from os import environ, stat, scandir, getlogin, remove, walk
from os.path import exists, dirname, realpath, expanduser, join
from pathlib import Path
from pprint import pprint
from re import match
from shutil import register_unpack_format, unpack_archive
import time
from typing import Any
import xml.etree.ElementTree as ET
from zipfile import ZipFile

import numpy as np
import pandas as pd
from py7zr import unpack_7zarchive
from pytz import common_timezones, timezone as tze
from rich import print
from rich.panel import Panel
from rich.box import SQUARE
from tqdm import tqdm
from unidecode import unidecode
import untangle
import xmltodict


def test_7z() -> None:
    """Test 7z archive extraction.
    https://py7zr.readthedocs.io/en/latest/api.html#py7zr.unpack_7zarchive
    """
    def ensure_7z_registered() -> None:
        """Formats registration must happen only once in a program.
        """
        try:
            register_unpack_format("7zip_custom", [".7z"], unpack_7zarchive)
        except ValueError:
            print("7z format already registered.")

    home = Path.home()
    file = Path(rf"{home}/Documents/test_7z.7z")

    extrac_dir = rf"{home}/Documents/test_7z_extracted"
    # create the directory if it doesn't exist
    Path(extrac_dir).mkdir(parents=True, exist_ok=True)
    ensure_7z_registered()
    try:
        # reading zip
        unpack_archive(file, extrac_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except IndexError as e:
        print(f"Error: {e}")
        raise
    except Exception as e:
        print(f"{e}\nProblem while extracting flie(s) from archive.")
        raise


def test_environ() -> None:
    """Test that the environment variable is set."""
    dico = {
        "One": 1,
        "Two": 2,
        "Three": 3,
    }
    # populate environment variable with the dico
    for key in dico:
        environ[f"Test_{key}"] = str(dico[key])

    # get process environment values
    for idx, key in enumerate(environ, 1):
        print(f"{idx:>3} {key}={environ[key]}")

    print()
    # get process environment values for only local environnement variables
    for idx, key in enumerate(environ, 1):
        if key.startswith("Test_"):
            print(f"{idx:>3} {key}={environ[key]}")


class Student(object):
    """Demonstration of instance method, class method and static method.
    https://codingdojo.org/kata/Student/
    """
    # class variable
    school_name = "ABC School"

    # constructor
    def __init__(self, name: str, age: int) -> None:
        # instance variables
        self.name = name
        self.age = age

    def show(self) -> None:
        """Show instance variables."""
        print(f"Name: {self.name}, Age: {self.age}, School: {Student.school_name}")

    @classmethod
    def change_school(cls, name: str) -> None:
        """Change the school name for all instances of the class.

        :param name: New school name
        """
        cls.school_name = name

    @staticmethod
    def find_notes(subject_name: str) -> list[str]:
        """Find notes for a given subject_name.

        :param subject_name: Name of the subject
        :returns: List of notes for the subject
        """
        # For demonstration purposes, return a static list of notes
        notes = {
            "Math": ["Algebra", "Geometry", "Calculus"],
            "Science": ["Physics", "Chemistry", "Biology"],
            "History": ["Ancient", "Medieval", "Modern"],
        }
        return notes.get(subject_name, [])


def test_student() -> None:
    """Test the Student class."""
    # Create instances of Student
    student1 = Student("Alice", 20)
    student2 = Student("Bob", 22)

    # Show initial details
    student1.show()
    student2.show()

    # Change school name using class method
    Student.change_school("XYZ University")

    # Show updated details
    student1.show()
    student2.show()

    # Find notes for a subject using static method
    math_notes = Student.find_notes("Math")
    print(f"Math Notes: {math_notes}")


def test_static_method() -> None:
    """Function to test a static method."""
    class C(object):
        """Thanks to @staticmethod, the function add() of the class C
        can be called without creating an instance of the class.
        """
        @staticmethod
        def add(a: int, b: int) -> int:
            """Add two numbers.

            :param a: First number
            :param b: Second number
            :returns: Sum of a and b
            """
            return a + b

    print("Use of a class static methode.")
    print(f"Result of add(12, 15) = {C.add(12, 15)}")


def make_constant() -> None:
    """How to create a real constant with the decorator @dataclass."""
    @dataclass(frozen=True)
    class ConstantNameSpace(object):
        """A class to hold constant values."""
        VALUE = 42

    print("\n-- Basic constant declared with a name in full capital.")
    D = "Toto"
    print(f"D={D}")
    D = "Tata"
    print(f"After modification\nD={D}")
    print("D isn't really a constatn because it can be modified."
          "\n==> python language is designed this way: "
          "names can always be reassigned."
          )
    print("\n-- Constant declared with a the dedicated class ConstantNameSpace --")
    C = ConstantNameSpace()
    print(f"C.VALUE={C.VALUE}")
    print("Trying to change the value of C value leads to this:")
    try:
        C.VALUE = 100
    except Exception as e:
        print(f"Error: {e}")


def compute_duration(logger: Logger,
                     measure_name: str,
                     started_time: dt
                     ) -> None:
    """Compute the duration of a process (function or a block of code).
    Log info in the form "Duration : 1m 14s 31ms".

    :param logger: Logger object to log the duration
    :param measure_name: Name of the process being measured
    :param started_time: Start time of the process
    """
    now = dt.now()
    duration_seconds = (now - started_time).total_seconds()
    hours, remainder = divmod(duration_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    seconds_int = int(seconds)
    ms = int((seconds - seconds_int) * 1000)

    parts = []
    if hours:
        parts.append(f"{int(hours)}h")
    if minutes:
        parts.append(f"{int(minutes)}m")
    parts.append(f"{seconds_int}s {ms}ms")

    logger.info(f"[{measure_name.upper():<7}] Duration: {" ".join(parts)}")


def is_valid_email(mail: str) -> bool:
    """How to validate astring a valid email.

    :param mail: email to check
    :returns: True if mail is valid otherwise false
    """
    adresse_ok = match(
        r"^[^@%§! #$^&*=()[\]<>;/\"?]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]{2,}$",
        mail
    )

    return bool(adresse_ok)


def test_is_valid_email() -> None:
    """Function to test is_valid_email()."""
    adresses = [
        "christian_martin@gmail.com",
        "JaiOublieLarobasegmail.com",
        "MarieHutchinson03523@yahoo.co.uk"
        "UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com",
        "ceciNestPasUneAdresseMail",
        "adresse mail.invalide@test.com",
        "addres?invalid@socgen.com"
    ]

    for a in adresses:
        print(f"{a} is {'valid' if is_valid_email(a) else 'invalid'}.")
        # should obtain:
        # christian_martin@gmail.com is valid",
        # JaiOublieLarobasegmail.com is invalid
        # MarieHutchinson03523@yahoo.co.uk is valid
        # UnEaDreSSeMail!38BIZarre@unSiTeBizarre.com"is invalid
        # ceciNestPasUneAdresseMail" is invalid
        # adresse mail.invalide@test.com"is invalid
        # addres?invalid@socgen.com is invalid


def time_zone(string_date: str) -> dt:
    """Get localized time.

    :param string_date: date as a string
        with format "%a %b %d %H:%M:%S %Y %Z"
        e.g."Thu Jun 13 16:37:57 2024 CEST"\n
    :returns localized time from Time zone name
    """
    timezones = defaultdict(list)
    for name in common_timezones:
        timezone = dtz.gettz(name)
        try:
            now = dt.now(timezone)
        except ValueError:
            continue
        abbrev = now.strftime("%Z")
        timezones[abbrev].append(name)

    date_string, tz_string = string_date.rsplit(" ", 1)
    date = dt.strptime(date_string, "%a %b %d %H:%M:%S %Y")
    tz = tze(timezones[tz_string][5])
    return tz.localize(date)


def filter_dictionary() -> None:
    """How to filter a dictionary with dictionary comprehension,
    like we did for a list.
    """
    objet = {
        "car01": 1,
        "car02": 2,
        "car03": 3,
        "plane01": 5,
        "plane02": 6,
        "plane03": 7,
    }
    result = {key: value for key, value in objet.items() if key.startswith("car")}
    print(result)


def remove_accents(input_str: str) -> str:
    """Remove accents fro many character in input_str.

    :param input_str: string in which to replace accented characters
    :returns input_str without accented characters
    """
    return unidecode(input_str)


def inverted_index() -> None:
    """https://pynative.com/intermediate-python-exercises/
    Exercise 12: Inverted __index__
    Practice Problem: create a fucntion that "inverts" a dictionary.
    Convert a dictionary of Author: [List of books] into a dictionary of Book: Author.
    This is the logic behind ho wsearch engines work! An inverted Index allows you
    to search for a term (the book) and immediately find where it belongs (the author).
    It emphasizes the use of nested loops and dictionary assignment.
    """
    def invert_dict(dico: dict) -> dict:
        """Inverts a dictionary : switch key and value.

        :param dico : dictionary to invert_dict
        :return the inverted dictinary
        """
        inverse_dict = {}
        for auteur, titres in dico.items():
            for titre in titres:
                inverse_dict[titre] = auteur

        return inverse_dict

    given_input = {
        "Orwell": ["1984", "Animal Farm"],
        "Huxley": ["Brave New World"]
    }

    print(given_input)
    print(invert_dict((given_input)))


def test_closure() -> None:
    """From https://www.geeksforgeeks.org/python/python-closures/.
    """
    def make_counter() -> Callable:
        """Outer function which will remember value.

        :returns last value of the function
        """
        # this variable will be remembered
        count = 0
        def counter() -> int:
            """The "real" function."""
            # modify outer variable
            nonlocal count
            count = 1
            return count

    counter1 = make_counter()
    print(counter1())
    print(counter1())
    print(counter1())
    print(counter1())


def use_decorator() -> None:
    """From https://www.geeksforgeeks.org/python/decorators-in-python/."""
    def decorator(func: Any) -> Any:
        """A decorator."""
        def wrapper() -> Any:
            """The wrapper."""
            print("Before calling the function.")
            func()
            print("After calling the function.")
        return wrapper

    def greet_1() -> None:
        """Function 1."""
        print("Hello, World!")
    greet_1()

    print()

    # applying the decorator to a function
    @decorator
    def greet_2() -> None:
        """Function 2."""
        print("Hello, World!")

    greet_2()


def use_numpy_arrays() -> None:
    """From https://www.geeksforgeeks.org/python/python-arrays/.
    """
    seq_array = np.arange(12).reshape(3, 4)
    rng = np.random.default_rng(0)
    random_array_1 = rng.integers(1, 100)
    random_array_2 = rng.integers(1, 100, size=(3, 4))
    print("seq_array")
    print(seq_array)
    print("random_array_1")
    print(random_array_1)
    print("random_array_2")
    print(random_array_2)

    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("a")
    print(a)


def arrondis()-> None:
    """How to round decimals correctly with python."""
    val = 2.6754

    print(f"Le chiffre de référence est {val}.\n")
    print("Avec round()")
    print(round(val, 2))

    print("\nAvec Decimal()")
    # use a chain to avoid binary errors
    x = Decimal(str(val))
    print("Three decimals")
    print(x.quantize(Decimal("0.000"), rounding=ROUND_HALF_UP))

    print("Two decimals")
    print(x.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP))

    print("One decimal")
    print(x.quantize(Decimal("0.0"), rounding=ROUND_HALF_UP))


def test_tqdm() -> None:
    """Testing tqdm library.
    Shows a smart progress meter in any console or GUI.
    """
    for _ in tqdm(range(50)):
        # simule une tâche longue
        time.sleep(0.1)


def test_rich() -> None:
    """Writing rich text to the terminal."""
    print(Panel.fit("[bold yellow]Hi, I'm a Panel",
                    border_style="green"))
    print(Panel.fit(
        "[italic red]Hi[/italic red], [italic blue]"
        "I'm another Panel[/italic blue]",
        border_style="red",
        box=SQUARE)
    )
    print(Panel.fit("With figures:\n1\n2\n3\n4\n5"))


def read_json() -> None:
    """Read a JSON file and print its content."""
    un_onglet_path = Path("~/.config/window_positions/window_positions_1_onglet_nemo.json").expanduser()
    if not un_onglet_path.exists():
        print(f"File {un_onglet_path} does not exist.")
        return

    try:
        data = pd.read_json(un_onglet_path, orient="records")
        print(data)
        data.to_excel("window_positions_records_1_onglet.ods", engine="odf", index=False)
    except Exception as e:
        print(f"Error reading JSON with orient='records': {e}")

    deux_onglets_path = Path("~/.config/window_positions/window_positions_2_onglet_nemo.json").expanduser()
    if not deux_onglets_path.exists():
        print(f"File {deux_onglets_path} does not exist.")
        return

    try:
        data = pd.read_json(deux_onglets_path, orient="records")
        print(data)
        data.to_excel("window_positions_records_2_onglets.ods", engine="odf", index=False)
    except Exception as e:
        print(f"Error reading JSON with orient='records': {e}")


def test_zipfile() -> None:
    """Test unpacking a zip file."""
    file = Path("~/Documents/Data.zip").expanduser()
    if not file.exists():
        print(f"File {file} does not exist.")
        return

    mkdir_path = file.parent / "extracted_zip"
    mkdir_path.mkdir(exist_ok=True)

    try:
        with ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(mkdir_path)
            print(f"Extracted files from {file} to {mkdir_path}")
    except Exception as e:
        print(f"Error extracting zip file: {e}")
        raise


def test_logger() -> None:
    """Function to show how to set up a simple
    logger over multiple modules."""
    import test_logger_module_1
    import test_logger_module_2
    import test_logger_module_3

    def setup_logger() -> Logger:
        """Logger setting up."""
        logger = getLogger("TestLoggerIn_test_core")
        if not logger.handlers:
            logger.setLevel(INFO)
            handler = StreamHandler()
            formatter = Formatter("[%(name)-30s] %(asctime)s - %(name)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            # Prevent log messages from being propagated to the root logger
            logger.propagate = False

        return logger

    logger = setup_logger()

    logger.info("Début du processus.")
    test_logger_module_1.fonction_1()
    test_logger_module_2.fonction_2()
    test_logger_module_3.fonction_3()
    logger.info("Fin du processus.")


def test_calendar() -> None:
    """Testing calendar module.
    Usefull to know how many days tere are in a given month.
    """
    month_table = {
        "January": "Janvier",
        "February": "Février",
        "March": "Mars",
        "April": "Avril",
        "May": "Mai",
        "June": "Juin",
        "July": "Juillet",
        "August": "Août",
        "September": "Septembre",
        "October": "Octobre",
        "November": "Novembre",
        "December": "Décembre"
    }
    year = dt.today().year
    for i in range(1, 13):
        nb_jours = calendar.monthrange(year, i)
        print(f"{month_table[calendar.month_name[i]]} {str(year):<15}{nb_jours[1]}")

    cal = calendar.TextCalendar(calendar.MONDAY)
    print()
    calendar.TextCalendar.prmonth(cal, theyear=year, themonth=dt.today().month)
    print()
    calendar.TextCalendar.prmonth(cal, theyear=2026, themonth=12)


if __name__ == "__main__":
    print(time_zone("Thu Jun 13 16:37:57 2024 CEST"))
