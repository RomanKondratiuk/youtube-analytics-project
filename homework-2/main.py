from src.channel import Channel

if __name__ == '__main__':
    dubrovskiy = Channel('UC9XJvt8OT-9_8QHDBdqocaw')
    dubrovskiy.print_info()

    # получаем значения атрибутов

    print(f'ID канала: "{dubrovskiy.id}"') # ID канала
    print(f'название канала: "{dubrovskiy.title}"') # название канала
    print(f'описание канала: "{dubrovskiy.description}"') # описание канала
    print(f'ссылка на канал: "{dubrovskiy.url}"')  # ссылка на канал
    print(f'количество подписчиков: "{dubrovskiy.subscriberCount}"')  # количество подписчиков
    print(f'количество видео: "{dubrovskiy.video_count}"')  # количество видео
    print(f'общее количество просмотров: "{dubrovskiy.viewCount}"')  # общее количество просмотров

    #менять не можем
    dubrovskiy._channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    #можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

   # создаем файл 'dubrowskiy.json' в данными по каналу
    dubrovskiy.to_json('dubrowskiy.json')
