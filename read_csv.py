import csv
from pathlib import Path
from typing import Optional


DATA_PATH = str(Path.joinpath(Path(__file__).resolve().parent, 'data', 'raw_data.csv')) 


def read_csv(device_id: Optional[str] = None):
    """
    read raw data return a generator
    """
    with open(DATA_PATH) as f:
        for row in csv.reader(f):
            if device_id and row[0] != device_id:
                continue

            yield {
                'device_fk_id': row[0],
                'latitude': row[1],
                'longitude': row[2],
                'time_stamp': row[3],
                'sts': row[4],
                'speed': row[5],
            }

