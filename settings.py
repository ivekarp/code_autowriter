import json
import os.path

""" Функции для работы с настройками"""


def read_config():
    with open("config.json") as f:
        config = json.load(f)
    return config


def create_default_config():
    config = {"key":"shift", "speed":0.5, "delay":1}
    with open("config.json", "w") as f:
        json.dump(config, f)


def check_config():
    if os.path.exists("config.json"):
        return
    else:
        create_default_config()
