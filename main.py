import discord
from bot import MyBot
from config import token

if __name__ == '__main__':
    intents = discord.Intents.all()
    bot = MyBot(intents)

    # @bot.event
    # async def on_message(message):
    #     print(message)

    # @bot.event
    # async def on_typing(channel, user, when):
    #     print("Shas napechataen ")

    bot.run(token)