from src.channel import Channel

dybrovskiy = dybrovskiy

if __name__ == '__main__':
    # Создаем два экземпляра класса
    dubrovskiy = Channel('UC9XJvt8OT-9_8QHDBdqocaw')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')

    # Используем различные магические методы
    print(dybrovskiy)  # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    print(dybrovskiy + highload)  # 100100
    print(dybrovskiy - highload)  # -48300
    print(highload - dybrovskiy)  # 48300
    print(dybrovskiy > highload)  # False
    print(dybrovskiy >= highload)  # False
    print(dybrovskiy < highload)  # True
    print(dybrovskiy <= highload)  # True
    print(dybrovskiy == highload)  # False
    
