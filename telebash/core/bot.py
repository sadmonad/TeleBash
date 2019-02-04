import json
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger('TeleBashBot')


class Bot:
    def __init__(self, config_path):
        self.config = {}
        self._load_config(config_path)

    def _load_config(self, config_path):
        logger.info('Loading config...')
        try:
            with open(config_path) as config:
                self.config = json.load(config)
        except FileNotFoundError as e:
            logger.critical('Config file does not exist', exc_info=True)
