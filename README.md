## Setup
```
git clone https://github.com/ssiyad/car-red-srv car-red-srv
cd car-red-srv
pipenv install
pipenv run flask run        # or
pipenv run python app.py    # or
pipenv shell                # then
python app.py
```

## Endpoints

- `GET /devices/:device_id`

An API that takes device ID and returns device’s latest information in response
#### Example Response
```
{
  "device_fk_id": "6888",
  "latitude": "19.7290096282959",
  "longitude": "76.20492553710938",
  "speed": "0",
  "sts": "2021-10-23T13:14:04.365831Z",
  "time_stamp": "2021-10-23T04:55:53Z"
}
```

- `GET /devices/:device_id/movement`

An API that takes device ID and returns start location & end location for that device
#### Example Response
```
{
  "end": {
    "location": "(19.73518943786621, 76.18452453613281)",
    "sts": "2021-10-23T13:28:05.626486Z",
    "time_stamp": "2021-10-23T13:28:00Z"
  },
  "start": {
    "location": "(19.7290096282959, 76.20492553710938)",
    "sts": "2021-10-23T13:14:04.365831Z",
    "time_stamp": "2021-10-23T04:55:53Z"
  }
}
```

- `GET /devices/:device_id/locations`

An API that takes in device ID, start time & end time and returns all the location points
#### Query Params
```
start_date  date after which entries should start   # any common date format eg: 2022-07-13 19:50:12.527840
end_date    date before which entries should end    # any common date format eg: 2022-07-13 19:50:12.527840
```

#### Example Response
```
{
  "data": [
    {
      "device_fk_id": 6888,
      "latitude": 19.729045867919922,
      "longitude": 76.2049331665039,
      "speed": 4.0,
      "sts": "Sat, 23 Oct 2021 13:14:04 GMT",
      "time_stamp": "Sat, 23 Oct 2021 04:55:55 GMT"
    },
    {
      "device_fk_id": 6888,
      "latitude": 19.729093551635742,
      "longitude": 76.20492553710938,
      "speed": 6.0,
      "sts": "Sat, 23 Oct 2021 13:12:55 GMT",
      "time_stamp": "Sat, 23 Oct 2021 04:55:57 GMT"
    }
  ],
  "size": 2
}
```
