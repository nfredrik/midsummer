import calendar
from datetime import datetime, timedelta
from typing import Final


class MidsummerException(Exception):
    ...


FIRST_POSSIBLE_DAY: Final = 20
MIDSUMMER_MONTH: Final = 6
DAYS_IN_A_WEEK_ZERO_CNT: Final = 6


def midsummer_date(year: int) -> datetime:
    """
    Returns the date of the midsummer's day in a given year.

    Args:
        year (int): The year for which to calculate the midsummer's day.

    Raises:
        MidsummerException: If the input type or value is not valid.

    Returns:
        datetime: The date of the midsummer's day in the given year.

    Raises:
        ValueError: If the midsummer's day falls on a non-Friday.

    """
    try:
        start = datetime(year, month=MIDSUMMER_MONTH, day=FIRST_POSSIBLE_DAY)
    except TypeError:
        raise MidsummerException("Invalid type need to be positive integer")

    except ValueError:
        raise MidsummerException("Invalid value need to be positive integer")

    my_list = [
        start + timedelta(days=x) for x in range(DAYS_IN_A_WEEK_ZERO_CNT)
    ]
    return next(item for item in my_list if item.weekday() == calendar.FRIDAY)

    raise MidsummerException("Error, this could not happen!")
