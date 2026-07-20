"""Python exercices from various web sites.
"""
def entiers_multiples() -> None:
    """Les entiers naturels inférieurs à 10 multiples de 3 ou de 5 sont 3,5,6 et 9. Leur somme est égale à 23.
    Trouver la somme des entiers inférieurs à 1000 et multiples de 3 ou 5.
    https://python.dellasantina.corsica/defis/project-euler/1-10/exercices
    """
    result = 0
    for chiffre in range(1, 1000):
        if (chiffre % 3 == 0) or (chiffre % 5 == 0):
            result += chiffre

    print(result)


def number_to_lcd(number: int,
                  thousand_separator: bool = False
                  ) -> str:
    """From https://codingdojo.org/kata/NumberToLCD.

    Figures will be represented as follows:
     _     _  _     _  _  _  _  _ 
    | |  | _| _||_||_ |_   ||_||_|
    |_|  ||_  _|  | _||_|  ||_| _|

    Displays a number like on a LCD screen, 
    eventually with a thousand separator.

    A figure is made of three rows of signs.

    :param number: number to be displayed
    :param thousand_separator: displays numbers with a thousand separator if True, default is False
    :returns: a string representation of the number in LCD format
    """
    def add_thousand_separator(pos: int,
                               len_number: int,
                               thousand_separator: bool
                               ) -> str:
        """Adds a thousand separator if needed.

        :param pos: position of figure
        :param len_number: len of the number
        :param thousand_separator: displays numbers with a
        thousand separator if True, defaultS to False
        :returns: the separator, as three spaces, or an empty string
        """
        if pos and ((len_number - pos) % 3) == 0 and thousand_separator:
            return "   "
        return ""

    # LCD display patterns for each digit (3 rows)
    # first element of each item is the top row,
    # second is the middle row, third is the bottom row
    lcd_patterns = {
        0: [" _ ", "| |", "|_|"],
        1: ["   ", "  |", "  |"],
        2: [" _ ", " _|", "|_ "],
        3: [" _ ", " _|", " _|"],
        4: ["   ", "|_|", "  |"],
        5: [" _ ", "|_ ", " _|"],
        6: [" _ ", "|_ ", "|_|"],
        7: [" _ ", "  |", "  |"],
        8: [" _ ", "|_|", "|_|"],
        9: [" _ ", "|_|", " _|"],
    }

    # Handle negative numbers
    number_str = str(abs(number))
    len_number = len(number_str)
    result = []
    for row in range(3):
        line = ""
        for pos, digit in enumerate(number_str):
            line += add_thousand_separator(pos, len_number, thousand_separator)
            line += f"{lcd_patterns[int(digit)][row]}"
        result.append(line)

    result.append("\n")

    return "\n".join(result)


if __name__ == "__main__":
    nombre = "1234568790123456"
    for n in range(4, len(nombre) + 1):
        print(number_to_lcd(int(nombre[:n]), True))
