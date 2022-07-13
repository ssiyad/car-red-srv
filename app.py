from flask import Flask
from dotenv import load_dotenv

from usecases.device_latest import device_latest

load_dotenv()

app = Flask(__name__)


@app.route('/devices/<int:device_id>', methods=['GET'])
def device_latest_info(device_id):
    # return 204 (no content) if nothing found
    return device_latest(device_id) or ('', 204)

