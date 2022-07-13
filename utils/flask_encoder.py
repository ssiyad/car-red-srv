from datetime import date
from flask.json import JSONEncoder


class FlaskEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return o.isoformat()

        return super().default(o)
