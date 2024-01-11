"""Loop exercises."""


def sum_between(start: int, end: int) -> int:
    """
    Return sum of integers between start and end (both included).

    print(sum_between(3, 5)) => 3 + 4 + 5 = 12
    print(sum_between(5, 5)) => 5
    """
    total = 0
    for num in range(start, end+1):
        total += num
    return total


def sum_of_even_numbers(n: int) -> int:
    """
    Return sum of even numbers from 0 up to n (included).

    print(sum_of_even_numbers(5)) => 0 + 2 + 4 = 6
    print(sum_of_even_numbers(0)) => 0
    """
    total = 0
    for num in range(0, n+1, 2):
        total += num
    return total


def sum_of_multiples(n: int, end: int) -> int:
    """
    Return sum of numbers which are multiples of n between 0 and end (included).

    print(sum_of_multiples(3, 10)) => 18
    print(sum_of_multiples(7, 10)) => 7
    print(sum_of_multiples(11, 10)) => 0
    """
    total = 0
    for num in range(0, end+1, n):
        total += num
    return total


def cross_sum(numbers: str) -> int:
    """
    Return cross sum of numbers.

    print(cross_sum("1234")) => 10
    print(cross_sum("0")) => 0
    print(cross_sum("4129458")) => 33
    """
    total = 0
    for num in numbers:
        total += int(num)
    return total


def multiply_between(start: int, end: int) -> int:
    """
    Multiply all numbers between start and end (both included).

    print(multiply_between(1, 3)) => 6
    print(multiply_between(4, 14)) => 14529715200
    print(multiply_between(0, 7)) => 0
    """
    product = 1
    for num in range(start, end+1):
        product *= num
    return product


def make_hola_string(count: int) -> str:
    """
    Make hola string.

    print(make_hola_string(3)) => "holaholahola"
    print(make_hola_string(0)) => ""
    """
    result = ""
    for _ in range(count):
        result += "hola"
    return result


def compound_interest(amount: int, years: int, rate: int) -> float:
    """
    Calculate compound interest.

    print(compound_interest(100, 2, 2)) => 104.04
    print(compound_interest(2000, 6, 8)) => 3173.748645888
    """
    principal = amount
    for year in range(years):
        interest = principal * rate / 100
        principal += interest
    return principal


def remove_vowels(original_string: str) -> str:
    """
    Return the given string without vowels.

    print(remove_vowels("tere-tere")) => tr-tr
    print(remove_vowels("hklmn")) => hklmn
    print(remove_vowels("aauuiii")) => ""
    """
    vowels = "aeiouõäöü"
    result = ""
    for char in original_string:
        if char not in vowels:
            result += char
    return result


if __name__ == '__main__':
    print(sum_between(3, 5))  # => 3 + 4 + 5 = 12
    print(sum_between(5, 5))  # => 5
    
    print(sum_of_even_numbers(5))  # => 0 + 2 + 4 = 6
    print(sum_of_even_numbers(0))  # => 0

    print(sum_of_multiples(3, 10))  # => 3 + 6 + 9 = 18
    print(sum_of_multiples(7, 10))  # => 7
    print(sum_of_multiples(11, 10))  # => 0

    print(cross_sum("1234"))  # => 1 + 2 + 3 + 4 = 10
    print(cross_sum("0"))  # => 0
    print(cross_sum("4129458"))  # => 33

    print(multiply_between(1, 3))  # => 1 * 2 * 3 = 6
    print(multiply_between(4, 14))  # => 14529715200
    print(multiply_between(0, 7))  # => 0

    print(make_hola_string(3))  # => "holaholahola"
    print(make_hola_string(0))  # => ""

    print(compound_interest(100, 2, 2))  # => 104.04
    print(compound_interest(2000, 6, 8))  # => 3173.748645888
    
    print(remove_vowels("tere-tere"))  # => tr-tr
    print(remove_vowels("hklmn"))  # => hklmn
    print(remove_vowels("aauuiii"))  # => ""
