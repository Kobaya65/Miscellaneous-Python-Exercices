"""Module for testing miscellaneous functions."""
import calendar
from collections import Counter, defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime as dt
import dateutil.tz as dtz
from decimal import Decimal, ROUND_HALF_UP
from getpass import getpass
import heapq as hq
from html import entities as he
from json import dumps, loads
import locale
from logging import Logger, Formatter, StreamHandler, getLogger, INFO, DEBUG
from math import prod
from os import environ, stat, scandir, mkdir, getlogin, remove, walk
from os.path import exists, dirname, realpath, expanduser, join
from pathlib import Path
from pprint import pprint
import secrets
from shutil import register_unpack_format, unpack_archive
import string
import time
from sys import exit, stderr
import textwrap
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
            
            # reading zip
            register_unpack_format("7zip_custom", [".7z"], unpack_7zarchive)
        except ValueError:
            print("7z format already registered.")
    

    home = Path.home()
    file = Path(rf"{home}/Documents/test_7z.7z")

    extrac_dir = rf"{home}\Documents\test_7z_extracted"
    build_path(extrac_dir, is_last_item_file=False)
    ensure_7z_registered()
    try:
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


def build_path(path: str, is_last_item_file: bool = False) -> bool:
    """Build a path, creating directories as needed.

    :param path: The path to build.
    :param is_last_item_file: If True, the last item in the path is treated as a file.
    :returns: True if the path was created successfully, False otherwise.
    """
    create = False
    path_splitted = path.split("/")
    if is_last_item_file:
        path_splitted = path_splitted[:-1]
    complete_path = ""
    for subf in path_splitted:
        complete_path = join(complete_path, subf)
        if not exists(complete_path):
            try:
                mkdir(complete_path)
                create = True
            except Exception as e:
                print(f"Error creating directory {complete_path}: {e}")

    return create


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
        """Change the school name  for all instances of the class.

        :param name: New school name
        """

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


if __name__ == "__main__":
    make_constant()
