from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from bs4 import BeautifulSoup
import requests

def start(bot, update):
    update.message.reply_text(start_message.format(update.message.from_user.first_name))
    keyboard = [[InlineKeyboardButton("Top Hits", callback_data='Top')],
                [InlineKeyboardButton("Top Artists", callback_data='')]
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(time_message, reply_markup=reply_markup)
                              
start_message ="""Hello {}
    Please enter the singer followed by the title of the song. 
    e.g. the chainsmokers closer
    Add @youtube and sign in to your youtube account by entering /auth and /setting to get your respective song playlist! """

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))
		
def generateSiteFromInput(bot, update):
	inputMessage = update.message.text
	inputMessageTrim = inputMessage.strip()
	processedMessage = inputMessageTrim.replace(' ', '-')
	
	rootPage = "https://genius.com/"
	finalUrl = rootPage + processedMessage + "-lyrics"
	return finalUrl
	
def getSongLyrics(bot, update):
	finalUrl = generateSiteFromInput(bot, update)
	update.message.reply_text(
        'Your Url is {}'.format(finalUrl))
	

updater = Updater('329555371:AAG6VH8AiLUJJCF5Vp1tGcJ6TFymho-_ArU')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.dispatcher.add_handler(MessageHandler(Filters.text, getSongLyrics))

page = "https://genius.com/"
requestResult = requests.get(page)

requestHtmlContent = requestResult.content

soup = BeautifulSoup(requestHtmlContent, "html.parser")

updater.start_polling()
updater.idle()