import logging
import threading

class SingletonMeta(type):
    """ A thread-safe implementation of Singleton. """
    _instances = {}
    _lock = threading.Lock()  # Ensures thread-safety for singleton instances

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    """ Singleton Logger using Python's built-in logging module. """
    def __init__(self, name='Logger', level=logging.INFO, log_file='app.log'):
        self.logger = logging.getLogger(name)
        
        if not self.logger.hasHandlers():  # Prevent adding handlers if they already exist
            self.logger.setLevel(level)

            # Console Handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter(
                "%(asctime)s | %(levelname)s : %(message)s", 
                datefmt='%Y-%m-%d @ %H:%M:%S'  # Customize the date format here
            ))
            self.logger.addHandler(console_handler)

            # File Handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(logging.Formatter(  # Fixed this line
                "%(asctime)s | %(levelname)s : %(message)s", 
                datefmt='%Y-%m-%d @ %H:%M:%S'  # Customize the date format here
            ))
            self.logger.addHandler(file_handler)

    def get_logger(self):
        """ Returns the underlying logger instance. """
        return self.logger