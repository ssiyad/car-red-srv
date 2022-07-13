from flask import Flask

from usecases.device_latest import device_latest
from usecases.device_movement import device_movment
from utils.wrap_result import wrap_result


app = Flask(__name__)


@app.route('/devices/<int:device_id>', methods=['GET'])
def device_latest_info(device_id: int):
    return wrap_result(device_latest(device_id))


@app.route('/devices/<int:device_id>/movement', methods=['GET'])
def device_movement_info(device_id: int):
    return wrap_result(device_movment(device_id))

