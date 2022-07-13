import csv
from pathlib import Path
from typing import Optional
from datetime import datetime

import dateutil.parser


DATA_PATH = str(Path.joinpath(Path(__file__).resolve().parent, 'data', 'raw_data.csv')) 


def read_csv(
        device_id: Optional[int] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ):
    """
    read raw data return a generator
    """
    with open(DATA_PATH) as f:
        reader = csv.reader(f)

        # skip header
        next(reader, None)

        for row in reader:
            r = {
                'device_fk_id': int(row[0]),
                'latitude': float(row[1]),
                'longitude': float(row[2]),
                'time_stamp': dateutil.parser.parse(row[3]),
                'sts': dateutil.parser.parse(row[4]),
                'speed': float(row[5]),
            }

            if device_id and r.get('device_fk_id') != device_id:
                continue

            if start_date:
                time_stamp = r.get('time_stamp')
                if not time_stamp or time_stamp <= start_date: continue

            if end_date:
                time_stamp = r.get('time_stamp')
                if not time_stamp or time_stamp >= end_date: continue

            yield r

