from datetime import timedelta

from googleapiclient.discovery import build
from helper.youtube_api_manual import youtube
import os


class StartYoutube():
    api_key = os.getenv('YT_API_KEY')
    service = build('youtube', 'v3', developerKey=api_key)


class PlayList(StartYoutube):
    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.playlist_videos = youtube.playlistItems().list(playlistId=self.__playlist_id,
                                                            part='contentDetails,snippet, id, status',
                                                            maxResults=50,
                                                            ).execute()
        self.playlist_info = youtube.playlists().list(part='snippet',
                                                      id=self.__playlist_id,
                                                      maxResults=50,
                                                      ).execute()
        self.title = self.playlist_info['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = youtube.videos().list(part='contentDetails,statistics',
                                                    id=','.join(video_ids)
                                                    ).execute()
        self.__total_time = timedelta()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.url}', {self.title})"

    def __str__(self):
        return (f"Название плэйлиста:{self.title}.\n Id канала{self.url}.")

    @property
    def total_duration(self):
        for video_inf in self.video_response["items"]:
            time_video_str = video_inf['contentDetails']['duration']
            """Ищем время, путем взятия из строки, получая индексы необходимых отрезков через поиск"""
            """Для секунды"""
            if "M" and "S" in time_video_str:
                start_second = time_video_str.find("M") + 1
                end_second = time_video_str.find("S")
                video_second = int(time_video_str[start_second:end_second])
            else:
                video_second = 0
            """Для минут"""
            if "T" and "M" in time_video_str:
                start_minute = time_video_str.find("T") + 1
                end_minute = time_video_str.find("M")
                minute = int(time_video_str[start_minute:end_minute])
            else:
                minute = 0
            new_time = timedelta(minutes=minute, seconds=video_second)
            self.__total_time += new_time
        return self.__total_time

    def show_best_video(self):
        """Записываем в качестве начальных данных кол-во лайков и id первого видео"""
        chosen_video_id = self.video_response["items"][0]["id"]
        max_like = int(self.video_response["items"][0]["statistics"]["likeCount"])

        for video_inf in self.video_response["items"]:
            like_count = int(video_inf["statistics"]["likeCount"])
            if like_count > max_like:
                chosen_video_id = video_inf["id"]
        return f'https://youtu.be/{chosen_video_id}'


# pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
# print(pl.playlist_videos)
# print(pl.playlist_info)
# print(pl.title)
# print(pl.url)
# print(pl.video_response)
