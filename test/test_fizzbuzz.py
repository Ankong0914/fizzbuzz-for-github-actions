from src.fizzbuzz import fizzbuzz


def test_fizzbuzz():
    num = 3
    expected = "Fizz"
    actual = fizzbuzz(num)
    assert actual == expected

    num = 5
    expected = "Buzz"
    actual = fizzbuzz(num)
    assert actual == expected

    num = 15
    expected = "FizzBuzz"
    actual = fizzbuzz(num)
    assert actual == expected

    num = 1
    expected = "1"
    actual = fizzbuzz(num)
    assert actual == expected
