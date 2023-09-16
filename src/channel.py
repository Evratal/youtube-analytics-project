from googleapiclient.discovery import build

from helper.youtube_api_manual import youtube


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        pass

    def print_info(self) -> None:
        request = youtube.search().list(part="snippet", channelId=self.channel_id, maxResults=10, type="video")
        response = request.execute()
        return response
