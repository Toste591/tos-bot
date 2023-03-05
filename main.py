from discord.ext import commands
from discord import Intents
import os

intents = Intents.default()
bot = commands.Bot(command_prefix='!', description='TODO add description :)', intents=intents)


@bot.event
async def on_ready():
    print('Initialized!')


bot.run(token=os.getenv('BOT_TOKEN'))
