from discord.ext import commands
from discord import Intents, Message
import os

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', description='TODO add description :)', intents=intents)


@bot.event
async def on_ready():
    print('Initialized!')


@bot.event
async def on_message(message: Message):
    if message.author == bot.user:
        return
    print(f'read message: {message.content}')
    if 'what\'s updog' in message.content.lower():
        await message.channel.send('nothin\' much what\'s up with you, dog?')
    await bot.process_commands(message)


bot.run(token=os.getenv('BOT_TOKEN'))
