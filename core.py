"""Module for testing miscellaneous functions."""
from os import environ

def test_environ() -> None:
    """Test that the environment variable is set."""
    dico = {
        "One": 1,
        "Two": 2,
        "Three": 3,
    }
    # populate environment variable with the dico    
    for key in dico:
        environ[key] = str(dico[key])

    # get process environment values 
    for idx, key in enumerate(environ, 1):
        print(f"{idx:>3} {key}={environ[key]}")


if __name__ == "__main__":
    test_environ()
