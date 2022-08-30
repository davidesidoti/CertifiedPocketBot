from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

load_dotenv()
# Get the API token from the .env file.
DISCORD_TOKEN = os.getenv('discord_token')

# Create a new Discord client and connect to the server.
intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

# Remove the default help command.
bot.remove_command('help')


# ANCHOR - ping command
@bot.command(name='ping', description='Pong!', brief='Returns pong!')
async def _ping(ctx):
    """
    It sends a message to the channel the command was sent in, with a green embed that says "Pong! I'm
    working :)"

    :param ctx: The context of where the command was used
    """
    embed = discord.Embed(
        title='Pong!', description='Pong! I\'m working :)', color=discord.Color.green())
    embed.set_author(
        name="Working :)", icon_url="https://i.imgflip.com/5uscl9.png")
    embed.set_footer(text="Made by the incredibly smart and talented Beyza")
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    for guild in bot.guilds:
        print('Active in {}\n Member Count : {}'.format(
            guild.name, guild.member_count))


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
