"""Exercises from https://codingdojo.org."""

def diamond(letter: str) -> str:
    """Build a diamond with letters.
    From https://codingdojo.org/kata/Diamond/

    :param letter: chosen letter
    :returns: the diamond as a string
    """
    def make_row(rang: int,
                 ligne: int
                 ) -> str:
        """Build a row where the letter to display will be deduced from ligne.

        :param rang: rank of the letter in the alphabet
        :param ligne: index of the row and the letter to display
        :returns: the row with the given letter, which is deduced from the line number
        """
        return (f"{" " * (rang - ligne - 1)}{chr(ligne + 65)}"
                f"{" " * (ligne + ligne - 1)}{chr(ligne + 65)}\n")

    def make_a_row(rang: int) -> str:
        """Build the "A" row.

        :param rang: rank of the letter in the alphabet
        :returns: the "A" row
        """
        return f"{" " * rang}A\n"

    if not letter.isalpha() or len(letter) != 1:
        raise ValueError("Input MUST be a single letter from A to Z.")

    letter = letter.upper()
    if letter == "A":
        return "A"

    rang = ord(letter) - 64
    bottom_row = rang - 2
    solution = ""

    solution += make_a_row(rang - 1)
    # top of the diamond
    for ligne in range(1, rang):
        solution += make_row(rang=rang, ligne=ligne)
    # bottom of the diamond
    for ligne in range(bottom_row, 0, -1):
        solution += make_row(rang=rang, ligne=ligne)
    solution += make_a_row(rang - 1)

    return solution


def diamond_bis(motif: str,
                largeur: int
                ) -> str:
    """Build a diamond with a given character and a given size
    which must be an odd number.
    Inspired from https://codingdojo.org/kata/Diamond/.

    :param motif: character
    :param largeur: width of the diamond
    :returns: the diamond as a string
    """
    if largeur < 1 or largeur % 2 == 0:
        raise ValueError("The width must be a positive odd number.")
    if not motif:
        raise ValueError("The pattern cannot be empty.")

    lignes, ESP = [], " "
    # top of the diamond
    for i in range(1, largeur + 1, 2):
        lignes.append(f"{ESP * ((largeur - i) // 2)}{motif * i}")
    # bottom of the diamond
    for i in range(largeur - 2, 0, -2):
        lignes.append(f"{ESP * ((largeur - i) // 2)}{motif * i}")

    return "\n".join(lignes)


def dictionary_replacer(input: str,
                        dico: dict
                        ) -> str:
    """Change words surrounded by $ in "input", with the corresponding value from the dictionary.
    https://codingdojo.org/kata/DictionaryReplacer/

    :param input: the string where to replace values
    :param dico: dictionary containing terms to be replaced and their corresponding value
    :returns: changed string
    """
    import re

    res = input
    for m in re.finditer(r"\$([^$]*)\$", input):
        mot = m.group(0)
        repl = dico.get(mot[1:-1], "")
        res = res.replace(mot, repl)

    return res


class Greed():
    """Greed is a dice game.
    https://codingdojo.org/kata/Greed/
    """
    __bonus_triple = {
        1: 1000,
        2: 200,
        3: 300,
        4: 400,
        5: 500,
        6: 600,
    }
    # __total_bonus aims at keeping trace of all bonuses in the total score
    __total_bonus = {"Throw": [], "Scores": {}}

    def check_pairs(self, die_values: list[int]) -> None:
        """Check if there are three pairs in die_values.

        :param die_values: list of dice values
        """
        figures = {}
        for x in die_values:
            figures[x] = figures.get(x, 0) + 1

        if len(figures) == 3:
            three_pairs = True
            for x in figures:
                if figures[x] != 2:
                    three_pairs = False
                    break
            if three_pairs:
                self.__total_bonus["Scores"]["Three Pairs"] = 800

    def of_a_kind(self, die_values: list[int]) -> None:
        """Calculates extra bonus for 3/4/5/6 of a kind.
        - four-of-a-kind (Multiply Triple Score by 2)
        - five-of-a-kind (Multiply Triple Score by 4)
        - six-of-a-kind (Multiply Triple Score by 8)

        :param die_values: list of dice values
        """
        for face_value in range(1, 7):
            if die_values.count(face_value) == 3:
                self.__total_bonus["Scores"][f"Triple {face_value}"] = self.__bonus_triple[face_value]
            if die_values.count(face_value) == 4:
                self.__total_bonus["Scores"][f"4 of a kind {face_value}"] = self.__bonus_triple[face_value] * 2
            if die_values.count(face_value) == 5:
                self.__total_bonus["Scores"][f"5 of a kind {face_value}"] = self.__bonus_triple[face_value] * 4
            if die_values.count(face_value) == 6:
                self.__total_bonus["Scores"][f"6 of a kind {face_value}"] = self.__bonus_triple[face_value] * 8

    def score(self, die_values: list[int]) -> dict:
        """Returns throw of die score.

        :param die_values: list of dice values
        :returns: score or error as a dictionary
        """
        self.__total_bonus["Throw"] = die_values
        self.__total_bonus["Scores"] = {}

        if len(die_values) > 6:
            self.__total_bonus.pop("Scores")
            self.__total_bonus["Error"] = "/!\\ Maximum 6 values! /!\\"
            return self.__total_bonus

        # straight
        comp = die_values.copy()
        comp.sort()
        if comp == [1, 2, 3, 4, 5, 6]:
            self.__total_bonus["Scores"]["Straight"] = 1200

        # single one
        if die_values.count(1) == 1:
            self.__total_bonus["Scores"]["Single One"] = 100

        # single five
        if die_values.count(5) == 1:
            self.__total_bonus["Scores"]["Single Five"] = 50

        # triples and more
        self.of_a_kind(die_values)

        # 3 pairs
        self.check_pairs(die_values)

        return self.__total_bonus


def test_class_greed() -> None:
    """The only purpose of this function is to test the Greed() class."""    
    greed = Greed() 

    d1 = greed.score([6, 2, 1, 5, 4, 3])
    print(f"straight        {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([1, 1, 1, 5, 4, 3])
    print(f"triple          {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([2, 2, 2, 5, 4, 3])
    print(f"triple          {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([3, 3, 3, 5, 4, 2])
    print(f"triple          {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([4, 4, 4, 5, 6, 3])
    print(f"triple          {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([5, 5, 5, 6, 4, 3])
    print(f"triple          {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([6, 6, 6, 5, 4, 3])
    print(f"triple          {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([6, 2, 3, 3, 3, 3])
    print(f"4 of a kind     {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([4, 4, 1, 4, 4, 4])
    print(f"5 of a kind     {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([4, 4, 2, 4, 4, 4])
    print(f"5 of a kind     {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([2, 2, 2, 2, 2, 2])
    print(f"6 of a kind     {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([5, 5, 5, 5, 5, 5])
    print(f"6 of a kind     {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([6, 6, 1, 1, 4, 4])
    print(f"3 pairs         {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([6, 6, 1, 2, 4, 4])
    print(f"3 pairs         {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([1, 5])
    print(f"1 and 5         {sum(d1["Scores"].values()):>6}\n{d1}")

    d1 = greed.score([6, 2, 1, 5, 4, 3, 6])
    print(f"more than 6 die\n{d1}")

    del greed


def leap_year(year: int) -> bool:
    """Checks if a given year is leap or not.
    https://codingdojo.org/kata/LeapYears/
    - all years divisible by 400 ARE leap years (so, for example, 2000 was indeed a leap year),
    - all years divisible by 100 but not by 400 are NOT leap years
        (so, for example, 1700, 1800, and 1900 were NOT leap years, NOR will 2100 be a leap year),
    - all years divisible by 4 but not by 100 ARE leap years (e.g., 2008, 2012, 2016),
    - all years not divisible by 4 are NOT leap years (e.g. 2017, 2018, 2019),
    - years divisible by 4000 are NOT leap years.

    :param year: year
    :returns: Return True if year is a leap year else False
    """
    if not isinstance(year, int):
        raise TypeError("year MUST be a whole number.")

    res = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) and (year % 4000 != 0):
        res = True

    return res


if __name__ == "__main__":
    print(diamond("m"))
