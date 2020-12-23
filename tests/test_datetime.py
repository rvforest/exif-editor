from datetime import timedelta
import exif_editor as ee


def test_add_mo_to_str():
    offset = timedelta(days=30, hours=12)
    assert ee.offset_datetime(b'2020:08:01 10:01:00', offset) == b'2020:08:31 22:01:00'
    assert ee.offset_datetime(b'2020:11:01 10:01:00', offset) == b'2020:12:01 22:01:00'
    assert ee.offset_datetime(b'2020:12:02 14:01:00', offset) == b'2021:01:02 02:01:00'
