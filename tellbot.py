from json import load
from threading import Event

from telegram import Update
from telegram    import Bot
from telegram.utils.request import Request
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters

with open("creds.json") as file:
    data = load(file)

code_glob = None
request = Request(proxy_url='socks5://localhost:2080')
bot = Bot(token=data["telbottoken"])#, request=request
updater = Updater(token=data["telbottoken"], use_context=True)#, request_kwargs={'proxy_url': 'socks5://localhost:2080'}
code_event = Event()

def sendtoadmin(text):
    bot.send_message(chat_id=data["admin"], text=text)

def echo(update: Update, context: CallbackContext):
    global code_glob
    code_glob = update.message.text

    try:
        int(code_glob)
    except:
        bot.send_message(chat_id=data["admin"], text="wtf ? ")
        return

    code_event.set()  # Set the event to signal that code_glob is ready


def getpin(pinurl):
    global code_glob
    
    if pinurl:
        bot.send_message(chat_id=data["admin"], text=f"get the pin\n\nlink: {pinurl}")
    if not code_event.wait(timeout=2):
        getpin(None)
    return code_glob

updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
updater.start_polling()