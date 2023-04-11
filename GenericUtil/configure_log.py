import logging
from datetime import datetime
import logging.handlers
import os
import inspect


def get_logger_instance():
    log_name = datetime.now().strftime('generated_logs_%H_%M_%d_%m_%Y.log')
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(f"../Logs/{log_name}")
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger