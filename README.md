# Midsummer Date Calculator

This Python module calculates the date of Midsummer's Day for a given year. Midsummer's Day typically falls on a Friday between June 20th and June 26th.

## Features

- **Custom Exception**: Includes a `MidsummerException` for handling errors specific to the Midsummer date calculation.
- **Type Checking**: Utilizes type hints for better code clarity and type checking.
- **Final Constants**: Employs `Final` from the `typing` module to declare constants.

## Usage

To use this module, simply import the `midsummer_date` function and pass the year for which you want to find the Midsummer's Day:

```python
    from midsummer import midsummer_date

    year = 2024
    print(midsummer_date(year))
```


## Functionality
The midsummer_date function calculates the date of Midsummer’s Day for the specified year. If the calculated date does not fall on a Friday, a ValueError is raised.

## Exceptions
MidsummerException: Raised if the input year is not an integer or if the date falls outside the expected range.
ValueError: Raised if the calculated Midsummer’s Day does not fall on a Friday, as per tradition.

## Constants
FIRST_POSSIBLE_DAY: The earliest possible day in June that Midsummer’s Day can fall on.
MIDSUMMER_MONTH: The month of June.
DAYS_IN_A_WEEK_ZERO_CNT: The number of days to check from the first possible day to find a Friday.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.