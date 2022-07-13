from typing import Any


def wrap_result(r: Any):
    # return 204 (no content) if nothing found
    return r or ('', 204)

