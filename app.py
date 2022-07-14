from flask import Flask, request, send_file

import dateutil.parser

from usecases.device_latest import device_latest
from usecases.device_movement import device_movement
from usecases.device_locations import device_locations
from utils.flask_encoder import FlaskEncoder
from utils.readme_html import readme_html
from utils.wrap_result import wrap_result


app = Flask(__name__)
app.json_encoder = FlaskEncoder


@app.route('/', methods=['GET'])
def index():
    return wrap_result(readme_html())


@app.route('/data', methods=['GET'])
def data_fetch():
    return send_file('data/raw_data.csv')


@app.route('/devices/<int:device_id>', methods=['GET'])
def device_latest_info(device_id: int):
    return wrap_result(device_latest(device_id))


@app.route('/devices/<int:device_id>/movement', methods=['GET'])
def device_movement_info(device_id: int):
    return wrap_result(device_movement(device_id))


@app.route('/devices/<int:device_id>/locations', methods=['GET'])
def device_locations_info(device_id: int):
    args = request.args;

    # use temp variables or python will complain about these being `str`
    _st = args.get('start_date')
    _en = args.get('end_date')

    start_date = end_date = None

    if _st:
        start_date = dateutil.parser.parse(_st)

    if _en:
        end_date = dateutil.parser.parse(_en)

    return wrap_result(device_locations(device_id, start_date=start_date, end_date=end_date))

