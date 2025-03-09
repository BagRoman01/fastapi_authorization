import logging
import os

import yaml


def setup_logging(default_path='../logging.yaml', default_level=logging.DEBUG):
    """Функция для загрузки конфигурации логирования из файла YAML"""
    absolute_path = os.path.abspath(default_path)
    print(f"Путь к конфигурационному файлу: {absolute_path}")
    try:
        # Пытаемся загрузить конфигурацию логирования из файла YAML
        with open(default_path, 'r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
    except FileNotFoundError:
        # Если файл конфигурации не найден, применяем базовую конфигурацию
        print(f"Лог файл {default_path} не найден. Применяется уровень по умолчанию.")
        logging.basicConfig(level=default_level)
    except yaml.YAMLError as exc:
        # Если файл невалиден, выводим ошибку
        print(f"Ошибка при загрузке YAML-конфигурации: {exc}")
        logging.basicConfig(level=default_level)