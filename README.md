## Setup
```
git clone https://github.com/ssiyad/car-red-srv car-red-srv
cd car-red-srv
pipenv install
pipenv run flask run    # or
python app.py
```

## Endpoints

- `GET /devices/:device_id`
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

