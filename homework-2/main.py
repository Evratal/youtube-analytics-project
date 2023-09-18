import os

from src.channel import Channel

if __name__ == '__main__':
    api_key = os.getenv('YT_API_KEY')
    moscowpython = Channel(api_key,'UC-OVMPlMA3-YCIeg4z5z23A')

    # получаем значения атрибутов
    print("---------------------------------")
    print(moscowpython.title)  # MoscowPython

    print("+++++++++++++++++++++++++++++++++")
    print(moscowpython.video_count)  # 685 (может уже больше)

    print("**********************************")
    print(moscowpython.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A

    # менять не можем
    moscowpython.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service(api_key))
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'moscowpython.json' в данными по каналу
    moscowpython.to_json('moscowpython.json')
