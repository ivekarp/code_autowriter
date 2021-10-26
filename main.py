"""
    Программа для автоматического переписывания текста в файл.
    Может пригодиться блогерам для иллюстрации программирования.
    Запускается с правами суперпользователя (требования модуля keyboard)

    Входной параметр: файл, с которого будет скопирован текст.

    При запуске программы нужно встать курсором в нужное место 
    и нажать горячую клавишу (в настройках можно её изменить)
    
    26.10.21 IveKarp
"""

import pyautogui as pg
import keyboard as kb
import os
import sys
from time import sleep
import threading
from settings import read_config, check_config


# Проверка и чтение файла настроек
check_config()
key, speed, delay = read_config().values()


def check_root():
    """ Проверяет права пользователя"""
    if os.geteuid() == 0:
        return
    else:
        print("Ошибка! Исполнять от имени суперпользователя!")
        exit(-1)


def check_file():
    """ Проверяет входной файл"""
    try:
        available_extensions = [".txt", ".py", ".c", ".cpp", ".h", ".html", ".css"]
        text_file = sys.argv[1]
        filename, file_extension = os.path.splitext(text_file)
        if file_extension in available_extensions:
            with open(text_file) as f:
                text = f.read()
            return text
        else:
            print("Ошибка! Расширение файла не поддерживается!")
            exit(-1)
    except IndexError:
        print("Ошибка! Нужно передать файл в программу!")
        exit(-1)



def all_ok():
    """ Если все проверки прошли"""
    print("Готов! Нажмите {}".format(key))


def start():
    while True:
        if kb.is_pressed(key):
            break
        elif kb.is_pressed("esc"):
            print("Exiting...")
            exit(0)


def autowrite(text):
    """ Пишущая функция"""
    sleep(delay)    
    pg.typewrite(text, speed)


def check_escape(th):
    """ Проверка нажатия escape для выхода из программы"""
    while True:
        if kb.is_pressed("esc") or not th.is_alive():
            print("Process stopped")
            exit(0)


def main():
    check_root()
    text = check_file()
    all_ok()
    start()
    th = threading.Thread(target = autowrite, args = [text], daemon = True)
    th.start()
    check_escape(th)


if __name__ == "__main__":
    main()
