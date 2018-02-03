from utilities.keys import Keys

from cyberbot.telebot import Telebot


def main():
    telebot = Telebot(Keys.BOT_TOKEN)
    telebot.run_update()


if __name__ == "__main__":
    main()
