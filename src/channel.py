import json
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        dict_to_print = {'kind': 'youtube#channelListResponse', 'etag': 'pYjb0XVs9dq2_Xawj-1sjUFZrM4', 'pageInfo': {'totalResults': 1, 'resultsPerPage': 5}, 'items': [{'kind': 'youtube#channel', 'etag': 'm1vtI03TiruCANlqXSqpJL4qMI4', 'id': 'UC9XJvt8OT-9_8QHDBdqocaw', 'snippet': {'title': 'Жекич Дубровский', 'description': 'Основной канал сообщества "Дубровский Синдикат"\n\nДУБРОВСКИЙ СИНДИКАТ - крупнейшее творческое объединение, основанное в 2017 году, включающее в себя десятки популярных каналов на YouTube и других соцсетях, собственное рекламное агентство, автосалоны и сервисы проката в разных городах мира, а так же ресурсы в\xa0сфере\xa0видеоигр.\n\nПо вопросам сотрудничества, спонсорства или рекламы, писать на почту dubrovskiysyndicate@mail.ru', 'customUrl': '@dubrovskiy-syndicate', 'publishedAt': '2013-03-06T02:05:58Z', 'thumbnails': {'default': {'url': 'https://yt3.ggpht.com/ytc/AGIKgqMt5pB_B63OOWd43dY5zGZAQSNczIi4rdM2Rd-DXQ=s88-c-k-c0x00ffffff-no-rj', 'width': 88, 'height': 88}, 'medium': {'url': 'https://yt3.ggpht.com/ytc/AGIKgqMt5pB_B63OOWd43dY5zGZAQSNczIi4rdM2Rd-DXQ=s240-c-k-c0x00ffffff-no-rj', 'width': 240, 'height': 240}, 'high': {'url': 'https://yt3.ggpht.com/ytc/AGIKgqMt5pB_B63OOWd43dY5zGZAQSNczIi4rdM2Rd-DXQ=s800-c-k-c0x00ffffff-no-rj', 'width': 800, 'height': 800}}, 'localized': {'title': 'Жекич Дубровский', 'description': 'Основной канал сообщества "Дубровский Синдикат"\n\nДУБРОВСКИЙ СИНДИКАТ - крупнейшее творческое объединение, основанное в 2017 году, включающее в себя десятки популярных каналов на YouTube и других соцсетях, собственное рекламное агентство, автосалоны и сервисы проката в разных городах мира, а так же ресурсы в\xa0сфере\xa0видеоигр.\n\nПо вопросам сотрудничества, спонсорства или рекламы, писать на почту dubrovskiysyndicate@mail.ru'}, 'country': 'RU'}, 'statistics': {'viewCount': '767257944', 'subscriberCount': '4640000', 'hiddenSubscriberCount': False, 'videoCount': '360'}}]}
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel_id = 'UC9XJvt8OT-9_8QHDBdqocaw'
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

