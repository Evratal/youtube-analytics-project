from googleapiclient.discovery import build
import json
import urllib.request
from helper.youtube_api_manual import youtube


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self,api_key, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        service = build('youtube', 'v3', developerKey=api_key)
        request = service.channels().list(id=channel_id, part = 'snippet,statistics')
        response = request.execute()
        #response_dict = json.load(response)
        self.title = response["items"][0]["snippet"]["title"]
        self.description = response["items"][0]["snippet"]["description"]
        self.url = f'https://www.youtube.com/channel/{channel_id}'
        self.subscriberCount = response["items"][0]["statistics"]["subscriberCount"]
        self.video_count = response["items"][0]["statistics"]["videoCount"]
        self.viewCount = response["items"][0]["statistics"]["viewCount"]

    def print_info(self) -> None:
        request = youtube.search().list(part="snippet", channelId=self.channel_id, maxResults=10, type="video")
        response = request.execute()
        return response

    @classmethod
    def get_service(cls, api_key):
        service = build('youtube', 'v3', developerKey=api_key)
        return service

    def to_json(self,name_file):
        id = self.__channel_id
        Title = self.title
        description = self.description
        url = self.url
        subscribe = self.subscriberCount
        video_count = self.video_count
        viewCount = self.viewCount
        mydict = {"id":id ,"title": Title, "description": description,"url":url,"subscribe":subscribe,"video_count":video_count,"viewCount":viewCount}
        with open(name_file, "w") as file:
            json.dump(mydict,file)