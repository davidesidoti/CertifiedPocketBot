from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

load_dotenv()
# Get the API token from the .env file.
DISCORD_TOKEN = os.getenv('discord_token')

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

bot.remove_command('help')


@bot.event
async def on_ready():
    for guild in bot.guilds:
        print('Active in {}\n Member Count : {}'.format(
            guild.name, guild.member_count))


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
