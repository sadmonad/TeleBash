from .executors import DummyExecutor


def command_hanlder(bot, update, user_data, cmd):
    cmd_result = DummyExecutor.execute(cmd)
    update.message.reply_text(cmd_result)
