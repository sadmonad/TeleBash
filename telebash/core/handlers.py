dummy_handler = lambda bot, update, user_data: update.message.reply_text('pop')

access_denied = lambda bot, update, user_data: update.message.reply_text('ACCESS_DENIED')
