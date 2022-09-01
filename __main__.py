from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import random

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
    embed.set_footer(
        text="Made by the incredibly smart and talented Beyza with the help of hashymashy :)")
    await ctx.send(embed=embed)


# ANCHOR - random command
@bot.command(name='random', description='Random number between a given range', brief='Returns a random number')
async def _random(ctx, min: int, max: int):
    """
    It sends a message to the channel the command was sent in, with a green embed that says "Pong! I'm
    working :)"

    :param ctx: The context of where the command was used
    :param min: The minimum number in the range
    :param max: The maximum number in the range
    """

    number = random.randint(min, max)

    embed = discord.Embed(
        title='The number is:', description=f'{number}', color=discord.Color.green())
    embed.set_author(
        name="Random", icon_url="https://preview.redd.it/6m34b658f4v71.jpg?width=640&crop=smart&auto=webp&s=a7d0300a0c937b32a2a9c09a37562e21de7ee275")
    embed.set_footer(
        text="Made by the incredibly smart and talented Beyza with the help of hashymashy :)")
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    """
    This function will print the name of the server and the number of members in the server when the bot
    is ready
    """
    for guild in bot.guilds:
        print('Active in {}\n Member Count : {}'.format(
            guild.name, guild.member_count))


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
