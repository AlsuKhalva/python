from telegram.ext import Updater, CommandHandler

PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


def greet_user(update, context):
    print('Вызван /start')


def main():
    mybot = Updater('1075777863:AAHjx-1GHr8loK1CdQpkxLE7inuliR-kVZk', use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    mybot.start_polling()
    mybot.idle()

main()