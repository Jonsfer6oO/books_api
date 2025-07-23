import logging
import logging.config

from fastapi import FastAPI

import API
from logs import conf

# Логирование
logging.config.dictConfig(conf)
main_logger = logging.getLogger(__name__)
main_logger.info('Старт приложения.')

main_logger.info('Создание экземпляра FastAPI')
app = FastAPI()
main_logger.info('Экземпляр FastAPI создан.')

# Подключение роутеров
main_logger.info('Подключение роутеров...')
app.include_router(API.db_router)
main_logger.info('Роутеры подключены.')