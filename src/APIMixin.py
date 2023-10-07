from googleapiclient.discovery import build

import os

class APIMixin:
    __API_KEY = os.getenv('YT_API_KEY')

    @classmethod
    def get_service(cls):
        service = build('youtube', 'v3', developerKey=cls.__API_KEY)
        return service