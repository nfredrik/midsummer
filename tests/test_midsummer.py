from datetime import datetime

import pytest
from assertpy import assert_that, soft_assertions

from midsummer import midsummer_date, MidsummerException


# from midsummer import midsummer_date
def test_midsummer_date():
    """Test midsummer date."""
    with soft_assertions():
        assert midsummer_date(year=2018) == datetime(2018, 6, 22)

        assert midsummer_date(year=2024) == datetime(2024, 6, 21)
        assert_that(midsummer_date(year=2024)).is_equal_to(datetime(2024, 6, 21))


def test_midsummer_date__invalid_type():
    with pytest.raises(MidsummerException):
        midsummer_date(year="2024")


def test_midsummer_date_negative():
    with pytest.raises(MidsummerException):
        midsummer_date(year=-2018)
