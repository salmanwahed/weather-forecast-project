import logging
from urllib.parse import urlencode
import requests
from django.conf import settings

logger = logging.getLogger('default')


class OpenWeathermapService:
    def __init__(self, lat, lon):
        self.app_id = settings.OPEN_WEATHERMAP_API_KEY
        self.base_url = settings.OPEN_WEATHERMAP_API_BASE
        self.lat = lat
        self.lon = lon

    def _get_api_url(self):
        params = dict(lat=self.lat, lon=self.lon, appid=self.app_id)
        return self.base_url + urlencode(params)

    def fetch_data(self):
        try:
            response = requests.get(self._get_api_url())
            if response.status_code in range(200, 300):
                return True, response.json()
            else:
                return False, response.json()
        except Exception as ex:
            logging.exception(ex)
        return False, None
