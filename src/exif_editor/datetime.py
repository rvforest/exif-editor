from datetime import datetime
from pathlib import Path

import piexif

# Exif Tags
# TODO: Are there other date time tags that need to be added?
DATETIME_ORIGINAL = 36867
DATETIME_DIGITIZED = 36868
DATETIME = 306


def offset_datetime(filename, offset):
    # Duplicate file before editing metadata
    file = Path(filename)

    # Parse Exif
    exif = piexif.load(str(file))

    # For each datetime tag, increment month by 1
    for tag in (DATETIME, DATETIME_DIGITIZED, DATETIME_ORIGINAL):
        # print(f"Tag: {tag}")
        if tag == DATETIME:
            keys = ("0th", "1st")
        else:
            keys = ("Exif",)

        for key in keys:
            # print(f"Key: {key}")
            try:
                exif[key][tag] = _offset_dt_str(exif[key][tag], offset)
            except KeyError:
                pass

    # Write back to file
    piexif.remove(str(file))  # TODO: Is this necessary?
    piexif.insert(piexif.dump(exif), str(file))


def _offset_dt_str(dt_str, offset):
    exif_dt_format = "%Y:%m:%d %H:%M:%S"
    dt = datetime.strptime(dt_str.decode(), exif_dt_format)
    new_dt = dt + offset
    return new_dt.strftime(exif_dt_format).encode()
