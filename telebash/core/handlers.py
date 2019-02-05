import logging

from .executors import DummyExecutor

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def command_hanlder(bot, update, user_data, cmd):
    logger.info(f'Executing command: {cmd.cmd}')
    cmd_result = DummyExecutor.execute(cmd)
    logger.info(f'Result: {cmd_result}')
    update.message.reply_text(cmd_result)
