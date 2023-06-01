import json
import os
from googleapiclient.discovery import build

from helper.youtube_api_manual import channel_id


class Channel:
    """Класс для ютуб-канала"""
    # атрибуты класса
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.

        """
        # инициализатор класса
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        dictionary = self.channel
        self.id = dictionary['items'][0]['id']
        self.title = dictionary['items'][0]['snippet']['title']
        self.description = dictionary['items'][0]['snippet']['description']
        self.url = dictionary['items'][0]['snippet']['thumbnails']['high']['url']
        self.subscriberCount = dictionary['items'][0]['statistics']['subscriberCount']
        self.video_count = dictionary['items'][0]['statistics']['videoCount']
        self.viewCount = dictionary['items'][0]['statistics']['viewCount']

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

