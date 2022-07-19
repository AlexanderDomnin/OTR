import requests
from typing import Union


class BaseApi:

    @staticmethod
    def get_status_code_response(url: Union[str, list]):
        if isinstance(url, list):
            status_code = [requests.get(url_number).status_code for url_number in url]
        else:
            status_code = requests.get(url).status_code
        return status_code

