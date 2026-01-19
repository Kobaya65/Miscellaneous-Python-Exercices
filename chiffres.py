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


def number_to_lcd(number: int) -> str:
    """Displays a number like on a lcd screen.
    From https://codingdojo.org/kata/NumberToLCD.
     _     _  _     _  _  _  _  _ 
    | |  | _| _||_||_ |_   ||_||_|
    |_|  ||_  _|  | _||_|  ||_| _|

    Args:
        number (int): number to be displayed

    Returns:
        str: string representation of the number in LCD format
    """
    # LCD display patterns for each digit (3 rows)
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
    result = []
    
    for row in range(3):
        line = "".join(lcd_patterns[int(digit)][row] for digit in number_str)
        result.append(line)
    
    return "\n".join(result)


if __name__ == "__main__":
    print(number_to_lcd(5168937425))
