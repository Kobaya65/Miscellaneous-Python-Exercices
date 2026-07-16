"""Various python challenges from python-fiddle.com
"""
from zipfile import ZipFile

def main() -> None:
    """https://python-fiddle.com/?checkpoint=1760713867
    """
    num_terms = 10
    fibonacci = [0, 1]

    while len(fibonacci) < num_terms:
        next_term = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_term)

    print(fibonacci)


def add(*args) -> float | int:
    """Adds an arbitrary number of arguments together and returns the sum.
    https://python-fiddle.com/challenges/add-args

    :param *args: The input arguments
    :returns: The sum of all the arguments
    """
    somme = 0
    for arg in args:
        somme += arg

    return somme


def find_substring(strings: list[str],
                   substring: str
                   ) -> bool:
    """Check if a substring is present in any string within a list.
    https://python-fiddle.com/challenges/check-substring-in-list

    :param strings: The list of strings to search within
    :param substring: The substring to search for
    :returns: True if the substring is found in any string, False otherwise
    """
    result = False
    for mot in strings:
        if substring in mot:
            result = True
            break

    return result


def ascii_value(char: str) -> int:
    """Returns the ASCII value of the given character.
    https://python-fiddle.com/challenges/ascii-value-of-character

    :param char: A single character
    :returns: The ASCII value of the character
    """
    res = ord(char)

    return res


def capital_words_spaces(input_string: str) -> str:
    """Insert spaces between words starting with capital letters in the given string.
    Use a regular expression to identify the pattern and insert spaces.
    https://python-fiddle.com/challenges/add-spaces-between-capital-words

    :param input_string: The input string containing words without spaces
    :returns: A new string with spaces inserted between capitalized words
    """
    import re

    pattern, res, pos = r"[A-Z]", "", 0
    for maj in re.finditer(pattern=pattern, string=input_string):
        # not to process first character if it is uppercase
        if maj.start():
            res += f"{input_string[pos:maj.start()]} "

        pos = maj.start()

    res += input_string[pos:]

    return res


def create_csv_file() -> None:
    """Create a csv file to be used in extract_column_from_csv().
    """
    import os.path
    import csv

    file_path = f"{os.path.expanduser("~")}/Documents/data.csv"
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
        writer.writeheader()
        writer.writerow({"Name": "John", "Age": "25", "City": "New York"})
        writer.writerow({"Name": "Emma", "Age": "30", "City": "London"})

    del os.path
    del csv


def extract_column_from_csv(file_path: str,
                            column_names: list[str]
                            ) -> list[dict]:
    """https://python-fiddle.com/challenges/csv-dict

    :param file_path: The path to the CSV file
    :param column_names: A list of column names to extract
    :returns: A list of dictionaries containing the values from the specified columns
    """
    import pandas as pd

    column_data = []
    df = pd.read_csv(file_path)
    df = df[column_names]

    for _, row in df.iterrows():
        entry = {col: row[col] for col in column_names}
        column_data.append(entry)
    
    return column_data


def map_folium() -> None:
    """https://python-fiddle.com/tutorials/folium"""
    import folium

    # Create a map centered at a given location
    m = folium.Map(location=[46.5887136, 0.3567401], zoom_start=20)

    folium.Marker(
        location=[46.58849, 0.358050],
        tooltip="Chambre Titouan",
        popup="Philippe AMICE<br />9 rue de provence<br />86000 Poitiers<br />",
        icon=folium.Icon(icon="home"),
    ).add_to(m)

    # Display the map
    m.save("map_Poitiers_Couronneries.html")
    m.show_in_browser()


def get_adjacent_coordinates(coord: tuple[int, int]) -> list[tuple[int, int]]:
    """Get all adjacent coordinates of a given coordinate.
    https://python-fiddle.com/challenges/adjacent-coordinates-extraction

    :param coord: The input coordinate as (x, y)
    :returns: A list of adjacent coordinates
    """
    if len(coord) != 2:
        raise ValueError("Input coordinate must be a tuple of two integers.")

    x, y = coord
    adjacent_coords = [
        (x, y - 1),     # Up
        (x, y + 1),     # Down
        (x - 1, y),     # Left
        (x + 1, y),     # Right
        (x - 1, y - 1), # Top-left
        (x + 1, y - 1), # Top-right
        (x - 1, y + 1), # Bottom-left
        (x + 1, y + 1), # Bottom-right
    ]

    return sorted(adjacent_coords)


def check_consecutive(lst: list) -> bool:
    """Check if the given list contains consecutive numbers.
    https://python-fiddle.com/challenges/check-consecutive-numbers

    :param lst: A list of integers.
    :returns: True if the list contains consecutive numbers, False otherwise.
    """
    consecutive = True
    lst.sort()
    for figure in range(1, len(lst)):
        if lst[figure] != lst[figure - 1] + 1:
            consecutive = False
            break

    return consecutive


def check_integer(text: str) -> bool:
    """Check if the given string represents a valid integer.
    https://python-fiddle.com/challenges/check-if-string-is-integer

    :param text: The input string to check.
    :returns: True if the string is a valid integer, False otherwise.
    """
    # strip any leading or trailing whitespace
    text = text.strip()
    try:
        _ = int(text)
        res = True
    except Exception:
        res = False

    return res 


def opposite_signs(x: int,
                   y: int
                   ) -> bool:
    """Check if two integers have opposite signs.
    https://python-fiddle.com/challenges/check-opposite-signs

    :param x: The first integer.
    :param y: The second integer.
    :returns: True if x and y have opposite signs,
                False otherwise or if at least one integer is zero.
    """
    if (x == 0 or y == 0):
        res = False
    else:
        res = (x > 0 and y < 0) or (x < 0 and y > 0)

    return res


def is_perfect_square(n: int) -> bool:
    """Determine if the given number is a perfect square.

    :param n: The number to check.
    :returns: True if n is a perfect square, False otherwise.
    """
    from math import sqrt

    if sqrt(n).is_integer():
        return True

    return False


def convert_list_dictionary(l1: list,
                            l2: list,
                            l3: list
                            ) -> list[dict]:
    """Convert three lists into a list of nested dictionaries.
    https://python-fiddle.com/challenges/convert-lists-to-nested-dictionary

    :param l1: List of keys for the outer dictionary.
    :param l2: List of keys for the inner dictionary.
    :param l3: List of values for the inner dictionary.
    :returns: A list of nested dictionaries.
    """
    res = []
    for i in range(len(l1)):
        res.append({l1[i]: {l2[i]: l3[i]}})

    return res


def check_char(string: str) -> str:
    """Check if the given string starts and ends with the same character.

    :param string: The input string to check.
    :returns: "Valid" if the string starts and ends with the same character, "Invalid" otherwise.
    """
    return "Valid" if (string[0] == string[-1]) else "Invalid"


def has_31_days(month_number: int) -> bool:
    """Determines whether a given month (represented by its number, 1 for January through 12 for December) has 31 days.
    Return True if the month has 31 days, and False otherwise.
    https://python-fiddle.com/challenges/check-month-days

    :param month_number: The number of the month (1-12)
    :returns: True if the month has 31 days, False otherwise
    """
    import calendar
    from datetime import datetime

    nb_jours = calendar.monthrange(datetime.today().year, month_number)[1]

    return nb_jours == 31


def reverse_vowels(s: str) -> str:
    """Reverse only the vowels in the input string.
    https://python-fiddle.com/challenges/reverse-vowels-in-string
    
    :param s: The input string.
    :returns: The string with vowels reversed.
    """
    vowels = "aàeéèëiïîoöôuüûyAEIOUY"
    deb, lon, fin = 0, len(s) - 1, len(s) - 1
    res = ""
    while deb <= lon:
        if s[deb] in vowels:
            while fin >= 0:
                if s[fin] in vowels:
                    # Swap the vowels
                    res += s[fin]
                    deb += 1
                    fin -= 1
                    break
                fin -= 1
        else:
            res += s[deb]
            deb += 1

    return res


def zip_n_files(*lists) -> None:
    """Zips an arbitrary number of files.

    :param *lists: the input paths
    """
    with ZipFile("/home/kobaya/Documents/output.zip", mode="w") as zp:
        for file in lists:
            zp.write(file)


def zip_lists(*lists) -> list[tuple]:
    """Zips an arbitrary number of lists together and returns the zipped list.

    :param: The input lists.
    :returns: The zipped list.
    """
    return list(zip(*lists))


if __name__ == "__main__":
    print(zip_lists([1, 2, 3], ['a', 'b', 'c'], [True, False, True]))
    print(zip_lists([1, 2, 3], ['a', 'b', 'c'], [True, False]))
