from src.channel import Channel


if __name__ == '__main__':
    # Создаем два экземпляра класса
    dubrovskiy = Channel('UC9XJvt8OT-9_8QHDBdqocaw')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')


    # Используем различные магические методы
    print(dubrovskiy)  # Жекич Дубровский, (https://yt3.ggpht.com/ytc/AGIKgqMt5pB_B63OOWd43dY5zGZAQSNczIi4rdM2Rd-DXQ=s800-c-k-c0x00ffffff-no-rj)
    print(dubrovskiy + highload)  # 4734600
    print(dubrovskiy - highload)  # 4585400
    print(highload - dubrovskiy)  # -4585400
    print(dubrovskiy > highload)  # True
    print(dubrovskiy >= highload)  # True
    print(dubrovskiy < highload)  # False
    print(dubrovskiy <= highload)  # False
    print(dubrovskiy == highload)  # False

