[![pypi](https://img.shields.io/pypi/v/midsummer.svg)](https://pypi.python.org/pypi/midsummer)
[![Downloads](https://static.pepy.tech/badge/midsummer)](https://pepy.tech/project/midsummer) 
[![Downloads](https://static.pepy.tech/badge/midsummer/month)](https://pepy.tech/project/midsummer)
[![versions](https://img.shields.io/pypi/pyversions/pydantic.svg)](https://github.com/midsummer/midsummer)

# Midsummer Date Calculator

This Python module calculates the date of Midsummer's Day for a given year. Midsummer's Day typically falls on a Friday between June 20th and June 26th.

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
**MidsummerException:** Raised if the input year is not an integer or if the date falls outside the expected range.
**ValueError:** Raised if the calculated Midsummer’s Day does not fall on a Friday, as per tradition.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
