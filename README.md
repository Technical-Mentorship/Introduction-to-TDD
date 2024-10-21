# Python Exercises - Unit Testing with TDD

This project demonstrates the use of **Test-Driven Development (TDD)** principles in Python. It includes a set of Python functions for common operations and unit tests that verify their correctness using the `unittest` framework.

**TIP: Use Ctrl+Shift+V to open this README in preview mode in your VS Code.**

## Project Structure

- **exercises.py**: Contains the implementations of the following functions:
  - `reverse_list(lst)`: Reverses the elements in a list.
  - `reverse_string(s)`: Reverses the characters in a string.
  - `is_english_vowel(c)`: Returns `True` if the character is an English vowel (case-insensitive), `False` otherwise.
  - `count_vowels(s)`: Counts the number of vowels in a given string.
  - `is_palindrome(s)`: Checks if a given string is a palindrome (case-insensitive, ignores spaces).
  - `find_minimum(lst)`: Finds and returns the minimum value from a list of numbers.
  - `sum_numbers(lst)`: Sums all the numbers in a list.
  - `factorial(n)`: Computes the factorial of a non-negative integer.

- **test_exercises.py**: Contains the unit tests for each of the functions using the `unittest` framework. It covers multiple edge cases and validates the correctness of each function.

## Test-Driven Development (TDD)

### What is TDD?

**Test-Driven Development (TDD)** is a software development process where you write tests for your code **before** writing the code itself. The TDD process is typically broken down into three main steps:

1. **Write a test**: You start by writing a failing test that describes a specific behavior or functionality you want your code to have.
2. **Make the test pass**: You then write just enough code to make the test pass, focusing only on the necessary implementation to fulfill the test.
3. **Refactor**: Once the test passes, you can refactor the code for optimization, readability, or better design, all while ensuring the tests still pass.

### Benefits of TDD

- **Improved code quality**: Since you write tests first, you design your code with testing in mind, resulting in cleaner, more modular code.
- **Fewer bugs**: Tests help catch errors early in the development process.
- **Confidence to refactor**: With a test suite in place, you can make changes or refactor code without fear of introducing regressions.

### TDD in This Exercise

In this exercise, we follow the TDD cycle for each function:

1. **Write the test**: Before implementing any function in `exercises.py`, we wrote a corresponding test in `test_exercises.py`. For example, the `test_reverse_list()` test checks that `reverse_list([1, 2, 3, 4, 5])` correctly returns `[5, 4, 3, 2, 1]`.

2. **Implement the code**: We then wrote the minimal code required to make each test pass. For example, the implementation of `reverse_list()` was written after writing its test.

3. **Refactor**: After the tests passed, we reviewed the implementation and optimized where necessary without changing the behavior.

## Running the Tests on the Terminal


1. Run the tests using the following command:

   ```
   python3 -m unittest test_exercises.py
   ```

## Configuring Tests in VSCode

If you are using Visual Studio Code with the Python extension installed, you can easily configure and run tests through the command palette. Here's how to set it up:

1. Open VSCode and ensure the Python extension is installed.
2. Open the command palette (press Ctrl+Shift+P).
3. Type `Python: Configure Tests` and select it.
4. Choose `unittest` as the test framework.
5. VSCode will search for tests in your project. Ensure that it detects the `test_exercises.py` file.
6. Once configured, you can run all tests or individual tests from the Testing sidebar in VSCode or through the command palette by selecting `Python: Run All Tests`.

   This will allow you to easily run, debug, and inspect test results directly within VSCode.
