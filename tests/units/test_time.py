from datetime import datetime

from freezegun import freeze_time


@freeze_time("2012-01-14")
def test_time_is_freeze():
    assert datetime.now() == datetime(2012, 1, 14)
