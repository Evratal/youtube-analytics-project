from googleapiclient.discovery import build
import json
import urllib.request
from helper.youtube_api_manual import youtube
import os


class Channel:
    """Класс для ютуб-канала"""

    api_key = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.api_key = Channel.api_key
        self.__channel_id = channel_id
        self.__service = build('youtube', 'v3', developerKey=self.api_key)
        request = self.__service.channels().list(id=channel_id, part='snippet,statistics')
        response = request.execute()
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

    def __str__(self):
        return (f"Название канала:{self.title}.\nОписание канала: {self.description}"
                f" ,\nКоличество подписчиков: {self.subscriberCount},\nКоличество видео на канале: {self.video_count},\n"
                f"Количество просмотров на канале: {self.viewCount}.")

    def __add__(self, other):
        """Суммарное количество просмотров двух каналов"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return int(subscriberCount_1) + int(subscriberCount_2)

    def __sub__(self, other):
        """Разница количества просмотров двух каналов"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return int(subscriberCount_1) - int(subscriberCount_2)

    def __eq__(self, other):
        """Сравнение на равенство"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return int(subscriberCount_1) == int(subscriberCount_2)

    def __lt__(self, other):
        """Сравнение операторов (меньше)"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return subscriberCount_1 < subscriberCount_2

    def __le__(self, other):
        """Сравнение операторов (меньше или равно)"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return int(subscriberCount_1) <= int(subscriberCount_2)

    def __gt__(self, other):
        """Сравнение операторов (больше)"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return int(subscriberCount_1) > int(subscriberCount_2)

    def __ge__(self, other):
        """Сравнение операторов (больше или равно)"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return int(subscriberCount_1) >= int(subscriberCount_2)

    @classmethod
    def get_service(cls, api_key):
        service = build('youtube', 'v3', developerKey=api_key)
        return service

    def to_json(self, name_file):
        id = self.__channel_id
        Title = self.title
        description = self.description
        url = self.url
        subscribe = self.subscriberCount
        video_count = self.video_count
        viewCount = self.viewCount
        mydict = {"id": id, "title": Title, "description": description, "url": url, "subscribe": subscribe,
                  "video_count": video_count, "viewCount": viewCount}
        with open(name_file, "w") as file:
            json.dump(mydict, file)
