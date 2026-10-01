# OOP Calculator

This project is a command-line calculator created for IS218 to practice object-oriented programming in Python. The project started with a simple addition object and was gradually expanded to include abstraction, inheritance, polymorphism, encapsulation, a command-line interface, error handling, testing, coverage, and continuous integration with GitHub Actions.

## Features

The calculator currently supports:

* Addition
* Subtraction
* Calculation history
* Removing calculations from history
* Help command
* Error handling for invalid input
* Error handling for invalid history removal
* Protection against non-finite numbers such as `nan` and `inf`
* Automated testing with pytest
* Test coverage checking
* Continuous integration with GitHub Actions

## Installation

Clone the repository:

```bash
git clone https://github.com/mmm286masud/calculator.git
```

Move into the project folder:

```bash
cd calculator
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Calculator

Run the calculator from the root of the project:

```bash
python -m calculator
```

The calculator supports these commands:

```text
add
subtract
history
remove
help
exit
```

Example:

```text
> add
First number: 10
Second number: 5
Result: 15

> subtract
First number: 20
Second number: 7
Result: 13
```

To view previous calculations:

```text
> history
```

To remove a calculation:

```text
> remove
```

To exit:

```text
> exit
```

## Running Tests

Run all tests with:

```bash
python -m pytest
```

The project uses pytest to test the calculation classes, history system, and command-line interface.

The project contains 37 test cases and requires 100% line and branch coverage.

## Project Structure

```text
calculator/
    __init__.py
    __main__.py
    calculation.py
    history.py
    cli.py

tests/
    test_calculation.py
    test_history.py
    test_cli.py

.github/
    workflows/
        tests.yml

pytest.ini
requirements.txt
README.md
```

## Design

### Calculation

`Calculation` is an abstract parent class that stores the two operands used by a calculation.

It also defines the common `get_result()` method that subclasses must implement.

### Add and Subtract

`Add` and `Subtract` inherit from `Calculation`.

Each subclass provides its own implementation of `get_result()`.

For example:

* `Add` adds the two operands.
* `Subtract` subtracts the second operand from the first.

This allows different calculation objects to be used through the same interface.

### History

The `History` class is responsible for storing and removing calculation objects.

Instead of allowing other parts of the program to directly control its internal list, it provides methods such as:

```text
add()
get_history()
remove()
```

This keeps responsibility for managing calculation history inside one class.

### CLI

The command-line interface connects the user to the calculator model.

It reads commands, creates the correct calculation object, stores calculations in history, and displays results.

It also handles invalid input so the application can continue running instead of crashing.

## Stage 6 Reflection

### 1. Where would Multiply belong?

I would create a `Multiply` class that inherits from `Calculation`, just like `Add` and `Subtract`.

It would implement its own `get_result()` method:

```python
class Multiply(Calculation):
    def get_result(self) -> float:
        return self.a * self.b
```

The CLI would also need to register the new command in its operations dictionary and add `multiply` to the help message.

Tests would need to be added to verify multiplication and make sure the CLI correctly creates and uses a `Multiply` object.

The `History` class would not need multiplication-specific code because it works with objects that follow the `Calculation` contract. It does not need to know whether an object represents addition, subtraction, multiplication, or another calculation.

### 2. How could the same idea apply to email and text notifications?

Email and text-message notification objects could share a common `send()` contract.

For example, a parent class could require:

```python
def send(self):
    ...
```

An `EmailNotification` class could implement `send()` by sending an email, while a `TextNotification` class could implement the same method by sending a text message.

Other parts of the application could then call:

```python
notification.send()
```

without needing to check which type of notification object it received.

This is similar to how the calculator can call `get_result()` on either an `Add` or `Subtract` object.

### 3. Which ideas transfer to another programming language?

The main design concepts in this project are not limited to Python.

Concepts such as:

* classes and objects
* inheritance
* abstraction
* encapsulation
* polymorphism
* separation of responsibilities
* automated testing
* continuous integration

can also be used in languages such as Java, C++, C#, and JavaScript.

However, I would still need to learn the syntax and rules of the new language.

For example, another language may have different rules for:

* declaring classes
* creating constructors
* defining abstract classes
* declaring types
* handling exceptions
* managing memory
* importing files and packages
* running tests

The design idea can remain similar even when the language syntax changes.

## Continuous Integration

The project uses GitHub Actions to automatically run the test suite whenever code is pushed or a pull request is created.

The workflow tests the project using multiple Python versions:

* Python 3.11
* Python 3.12
* Python 3.13
* Python 3.14

This helps confirm that the calculator continues to work correctly in a clean environment and across supported Python versions.
