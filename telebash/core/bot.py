import json
import logging

from .exceptions import ConfigUniqueTelegramCommandsError


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger('TeleBashBot')


class Config:
    def __init__(self, config_path, reload=False):
        self.path = config_path
        self._load(self.path, reload=reload)
        self._validate()

    def _load(self, config_path, reload=False):
        logger.info('Loading config...') if not reload else logger.info('Reloading config...')
        try:
            with open(config_path) as config:
                self._config = json.load(config)
        except FileNotFoundError:
            logger.critical('Config file does not exist', exc_info=True)
            exit(1)

    def _validate(self):
        logger.info('Validating config...')
        try:
            self.user_id = self._config['user_id']
            self.bot_token = self._config['token']
            self.commands = self._config['commands']

            exist = []

            for cmd in self.commands:
                if cmd not in exist:
                    exist.append(cmd)
                else:
                    raise ConfigUniqueTelegramCommandsError(
                        f'Not unique command: {cmd}', cmd
                    )

        except KeyError:
            logger.error('Required config field is missing', exc_info=True)
            exit(1)

        except ConfigUniqueTelegramCommandsError:
            logger.error('Duplicate command detected', exc_info=True)
            exit(1)


class Bot:
    def __init__(self, config_path):
        self._load_config(config_path)

    def _load_config(self, config_path, reload=False):
        self.config = Config(config_path)

    def reload_config(self, config_path=None):
        config_path = config_path if config_path is not None else self.config.path
        self._load_config(config_path, reload=True)
