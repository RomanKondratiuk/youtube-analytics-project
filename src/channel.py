import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    # атрибуты класса
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        # инициализатор класса
        self._channel_id = channel_id
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        dictionary = self.channel
        self.id = dictionary['items'][0]['id']
        self.title = dictionary['items'][0]['snippet']['title']
        self.description = dictionary['items'][0]['snippet']['description']
        self.url = dictionary['items'][0]['snippet']['thumbnails']['high']['url']
        self.subscriberCount = dictionary['items'][0]['statistics']['subscriberCount']
        self.video_count = dictionary['items'][0]['statistics']['videoCount']
        self.viewCount = dictionary['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f" {self.title}, ({self.url})"

    def __add__(self, other):
        return int(self.subscriberCount) + int(other.subscriberCount)

    def __sub__(self, other):
        return int(self.subscriberCount) - int(other.subscriberCount)
        return int(other.subscriberCount) - int(self.subscriberCount)

    def __gt__(self, other):
        return int(self.subscriberCount) > int(other.subscriberCount)

    def __ge__(self, other):
        return int(self.subscriberCount) >= int(other.subscriberCount)

    def __lt__(self, other):
        return int(self.subscriberCount) < int(other.subscriberCount)

    def __le__(self, other):
        return int(self.subscriberCount) <= int(other.subscriberCount)

    def __eq__(self, other):
        return int(self.subscriberCount) == int(other.subscriberCount)




    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        """метод to_json(), сохраняющий в файл значения атрибутов экземпляра Channel"""
        data = {
            "channel_id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriberCount": self.subscriberCount,
            "video_count": self.video_count,
            "viewCount": self.viewCount
        }
        with open(file_name, "w") as json_file:
            json.dump(data, json_file, ensure_ascii=False)
            return data

    @classmethod
    def get_service(cls):
        """класс-метод возвращающий объект для работы с YouTube API"""
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    @property
    def channel_id(self):
        return self._channel_id
