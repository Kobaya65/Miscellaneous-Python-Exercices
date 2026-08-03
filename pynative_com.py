"""From https://pynative.com/python-exercises-with-solutions/
"""
from box import Box
import json
import re


def exercise_1(phrase: str) -> str:
    """Reverse each word of a phrase.
    :param phrase: phrase to be reversed
    :returns: Reverse phrase
    """
    mots = phrase.split()
    results = []
    result = ""

    results = [mot[::-1] for mot in mots]

    result = " ".join(results)

    return result


def python_regex_exercises() -> None:
    """https://pynative.com/python-regex-exercises"""
    print("Exercise 2")
    test_strings = ["a", "ab", "abb", "abbb", "b", "ba"]
    for s in test_strings:
        # print(f"{s:<7} -> {"Match" if re.match(r"^a", s) else "No match"}")
        print(f"{s:<7} -> {"Match" if re.match(r"ab*", s) else "No match"}")
    
    print("\nExercise 3")
    for s in test_strings:
        print(f"{s:<7} -> {
                "Match" if re.match(r"ab+", s) else "No match"
            }"
        )
    
    print("\nExercise 4")
    for s in test_strings:
        print(f"{s:<7} -> {
                "Match" if re.fullmatch(r"ab?", s) else "No match"
            }"
        )
    
    print("\nExercise 5")
    for s in test_strings:
        print(f"{s:<7} -> {
                "Match" if re.fullmatch(r"ab{3}", s) else "No match"
            }"
        )
    
    print("\nExercise 6")
    for s in test_strings:
        print(f"{s:<7} -> {
                "Match" if re.fullmatch(r"ab{2,3}", s) else "No match"
            }"
        )

    print("\nExercise 7")
    test_strings = [
        "hello_world",
        "foo_bar",
        "hello",
        "hello_",
        "_world",
        "Hello_world",
        "hello_World"
    ]
    for s in test_strings:
        print(f"{s:<12} -> {
                "Match" if re.fullmatch(r"[a-zA-Z]+_[a-zA-Z]+", s) 
                else "No match"
            }"
        )

    print("\nExercise 8")
    test_strings = [
        "Hello",
        "World",
        "python",
        "HELLO",
        "Hello123",
        "H",
        "Ha"
    ]
    for s in test_strings:
        print(f"{s:<12} -> {
                "Match" if re.fullmatch(r"[A-Z][a-z]+", s) 
                        else "No match"
            }"
        )

    print("\nExercise 9")
    test_strings = [
        "a123b",
        "axyzb",
        "ab",
        "a b",
        "ab ",
        "b123a",
        "a123"
    ]
    for s in test_strings:
        print(f"{s:<12} -> {
                "Match" if re.fullmatch(r"^a.*b$", s) 
                        else "No match"
            }"
        )

    print("\nExercise 10")
    test_strings = [
        "Hello world",
        "Hello",
        "Say Hello",
        "hello world",
        "HelloWorld"
    ]
    for s in test_strings:
        print(f"{s:<12} -> {
                "Match" if re.fullmatch(r"^Hello\b.*", s) 
                        else "No match"
            }"
        )

    print("\nExercise 11")
    test_strings = [
        "I love Python",
        "Python is great",
        "I love Python!",
        "python",
        "I love Python."
    ]
    for s in test_strings:
        print(f"{s:<15} -> {
                "Match" if re.fullmatch(r".*Python[.,!?]?$", s) 
                        else "No match"
            }"
        )


def exercise_3(number_list: list[int]) -> list[int]:
    """Remove items from a list while iterating.
    In this question, you need to remove items from a list during iteration
    without creating a separate copy of the list.
    Remove numbers greater than 50.

    :param number_list: list of numbers to be processed
    :returns: processed list of numbers
    """
    return [nombre for nombre in number_list if nombre <= 50]


def name_and_age(name: str,
                 age : int
                 ) -> None:
    """https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-1-create-a-function-in-python
    exercise 1

    :param name: The name of the person.
    :param age: The age of the person.
    """
    print(f"Your name is {name} and you are {age} years old.")


def variable_length_of_arguments(*args) -> None:
    """https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-2-create-a-function-in-python-with-variable-length-arguments
    exercise 2

    :param *args: Variable length of arguments.
    """
    for value in args:
        print(value)


def return_multiple_values_from_a_function(a: int,
                                           b: int
                                           ) -> tuple[int, int]:
    """https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-3-create-a-function-in-python-that-returns-multiple-values
    exercise 3

    :param a: The first integer
    :param b: The second integer
    :returns: A tuple containing the sum and product of a and b
    """
    return (a + b, a * b)


def show_employee(name: str,
                  salary: int = 9000
                  ) -> None:
    """https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-4-create-a-function-in-python-with-default-arguments
    exercise 4

    :param name: The name of the employee.
    :param salary: The salary of the employee.
    """
    print(f"Employee Name: {name}, Salary: {salary}")


def outer_function(a: int,
                   b: int
                   ) -> int:
    """https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-5-create-an-inner-function-in-python
    exercise 5
    """
    def inner_function(a: int,
                       b: int
                       ) -> int:
        """Addition of a and b.

        :param a: first argument
        :param b: second ergument

        :returns: sum of the arguments
        """
        return a + b

    return inner_function(a, b) + 5


def sum_of_numbers(number: int) -> int:
    """https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-13-write-a-recursive-function-to-calculate-the-factorial
    exercise 6

    :param number: The number to calculate the sum of numbers up to.
    :returns: The sum of numbers from 1 to the given number.
    """
    if number <= 1:
        return number
    else:
        return number + sum_of_numbers(number - 1)


def create_a_lambda_function_that_squares_a_given_number() -> None:
    """https://pynative.com/python-functions-exercise-with-solutions/#h-exercise-1-create-a-function-in-python
    exercise 14
    """
    square = lambda x: x * x
    print(square(5))


def python_dictionary_exercise_with_solutions() -> None:
    """https://pynative.com/python-dictionary-exercise-with-solutions/
    """
    # exercises 1 & 2
    my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
    print(my_dict)
    my_dict["profession"] = "Doctor"
    print(my_dict)
    my_dict["age"] = 40
    print(my_dict)
    print(my_dict["city"])

    print("without profession")
    my_dict.popitem()
    print(my_dict)

    print("Printing all key-value pairs:")
    for x in my_dict:
        print(f"{x}: {my_dict[x]}")
    
    print(f"Does 'age' exist: {my_dict['age'] is not None}")
    print(f"Does 'age' exist: {'age' in my_dict}")

    # exercise 3
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    new_dict = dict(zip(keys, values))
    print(new_dict)


def python_json_exercise() -> None:
    """https://pynative.com/python-json-exercise/#h-exercise-1-convert-the-following-dictionary-into-json-format"""
    # exercise 5
    sampleJson = """{ 
        "company":{ 
            "employee":{ 
                "name":"emma",
                "payable":{ 
                    "salary":7000,
                    "bonus":800
                }
            }
        }
    }"""
    sample_json = json.loads(sampleJson)
    print(" json ".center(80, "-"))
    print(sample_json["company"]["employee"]["payable"]["salary"])

    print(" Box ".center(80, "-"))
    sample = Box(sample_json)
    print(sample.company.employee.payable.salary)

    # exercise 6
    class Vehicle:
        def __init__(self, name, engine, price):
            self.name = name
            self.engine = engine
            self.price = price

    vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

    # Convert it into JSON format
    vehicle_json = json.dumps(vehicle.__dict__)
    print("-" * 80)
    print(vehicle_json)


if __name__ == "__main__":
    python_json_exercise()
