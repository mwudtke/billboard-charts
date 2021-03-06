import datetime

import billboard
from nose.tools import raises


def test_date_rounding():
    """Checks that the Billboard website is rounding dates correctly: it should
    round up to the nearest date on which a chart was published.
    """
    chart = billboard.ChartData('hot-100', date='1000-10-10')
    assert chart.date == '1958-08-04'  # The first Hot 100 chart

    chart = billboard.ChartData('hot-100', date='1996-07-30')
    assert chart.date == '1996-08-03'


def test_datetime_date():
    """Checks that ChartData correctly handles datetime objects as the
    date parameter.
    """
    chart = billboard.ChartData('hot-100', datetime.date(2016, 7, 9))
    assert len(chart) == 100
    assert chart.date == '2016-07-09'


@raises(ValueError)
def test_unsupported_date_format():
    """Checks that using an unsupported date format raises an exception."""
    billboard.ChartData('hot-100', date='07-30-1996')


@raises(ValueError)
def test_empty_string_date():
    """Checks that passing an empty string as the date raises an exception."""
    billboard.ChartData('hot-100', date='')
