from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import random
import googletrans

load_dotenv()
# Get the API token from the .env file.
DISCORD_TOKEN = os.getenv('discord_token')

# Create a new Discord client and connect to the server.
intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

# Instantiate the Google Translator.
translator = googletrans.Translator()
translator.raise_Exception = True

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
    # Create the embed.
    embed = discord.Embed(
        title='Pong!', description='Pong! I\'m working :)', color=discord.Color.green())
    embed.set_author(
        name="v0.0.1", icon_url="https://i.imgflip.com/5uscl9.png")
    embed.set_footer(
        text="Made by the incredibly smart and talented Beyza with the help of hashymashy :)")

    # Send the embed.
    await ctx.send(embed=embed)


# ANCHOR - random command
@bot.command(name='random', description='Random number between a given range', brief='Returns a random number')
async def _random(ctx, min, max):
    """
    It sends a message to the channel the command was sent in, with a green embed that says "Pong! I'm
    working :)"

    :param ctx: The context of where the command was used
    :param min: The minimum number in the range
    :param max: The maximum number in the range
    """

    if not min or not max:
        embed = discord.Embed(
            title='Error', description='You need to specify a minimum and maximum number', color=discord.Color.red())
        embed.set_author(
            name='Random', icon_url='https://preview.redd.it/6m34b658f4v71.jpg?width=640&crop=smart&auto=webp&s=a7d0300a0c937b32a2a9c09a37562e21de7ee275')
        embed.set_footer(
            text='Made by the incredibly smart and talented Beyza with the help of hashymashy :)')
        await ctx.send(embed=embed)
        return

    if type(min) != int or type(max) != int:
        embed = discord.Embed(
            title='Error', description='The arguments must be numbers.', color=discord.Color.red())
        embed.set_author(
            name='Random', icon_url='https://preview.redd.it/6m34b658f4v71.jpg?width=640&crop=smart&auto=webp&s=a7d0300a0c937b32a2a9c09a37562e21de7ee275')
        embed.set_footer(
            text='Made by the incredibly smart and talented Beyza with the help of hashymashy :)')
        await ctx.send(embed=embed)
        return

    number = random.randint(min, max)

    embed = discord.Embed(
        title='The number is:', description=f'{number}', color=discord.Color.green())
    embed.set_author(
        name="Random", icon_url="https://preview.redd.it/6m34b658f4v71.jpg?width=640&crop=smart&auto=webp&s=a7d0300a0c937b32a2a9c09a37562e21de7ee275")
    embed.set_footer(
        text="Made by the incredibly smart and talented Beyza with the help of hashymashy :)")
    await ctx.send(embed=embed)


# ANCHOR - translate command
@bot.command(name='translate', description='Translate a given text to a given language', brief='Translates a given text')
async def _translate(ctx, lang, *, text):
    if lang == 'en':
        # Translate the text to English.
        translation = translator.translate(text, dest='en')
        # Create the embed.
        embed = discord.Embed(
            title='Translation', description=f'**Original text (from: [{translation.src}]):**\n{translation.origin}\n\n**Translation (to [{translation.dest}]):**\n{translation.text}\n\n**Pronunciation:**\n{translation.pronunciation}', color=discord.Color.green())
        embed.set_author(
            name="Translate", icon_url="https://assets.tes.com/magazine-attachments/s3fs-public/styles/article_image_mobile/public/media/image/archived/teacher_cat.jpg?itok=-XzA4-SL")
        embed.set_footer(
            text="Made by the incredibly smart and talented Beyza with the help of hashymashy :)")
        # Send the embed.
        await ctx.send(embed=embed)
    elif lang == 'de':
        # Translate the text to German.
        translation = translator.translate(text, dest='de')
        # Create the embed.
        embed = discord.Embed(
            title='Translation', description=f'**Original text (from: [{translation.src}]):**\n{translation.origin}\n\n**Translation (to [{translation.dest}]):**\n{translation.text}\n\n**Pronunciation:**\n{translation.pronunciation}', color=discord.Color.green())
        embed.set_author(
            name="Translate", icon_url="https://assets.tes.com/magazine-attachments/s3fs-public/styles/article_image_mobile/public/media/image/archived/teacher_cat.jpg?itok=-XzA4-SL")
        embed.set_footer(
            text="Made by the incredibly smart and talented Beyza with the help of hashymashy :)")
        # Send the embed.
        await ctx.send(embed=embed)
    elif lang == 'tr':
        # Translate the text to Turkish.
        translation = translator.translate(text, dest='tr')
        # Create the embed.
        embed = discord.Embed(
            title='Translation', description=f'**Original text (from: [{translation.src}]):**\n{translation.origin}\n\n**Translation (to [{translation.dest}]):**\n{translation.text}\n\n**Pronunciation:**\n{translation.pronunciation}', color=discord.Color.green())
        embed.set_author(
            name="Translate", icon_url="https://assets.tes.com/magazine-attachments/s3fs-public/styles/article_image_mobile/public/media/image/archived/teacher_cat.jpg?itok=-XzA4-SL")
        embed.set_footer(
            text="Made by the incredibly smart and talented Beyza with the help of hashymashy :)")
        # Send the embed.
        await ctx.send(embed=embed)
    else:
        # Create the embed.
        embed = discord.Embed(
            title='Error', description='The language you specified is not supported.\n\n**Available languages:**\nEnglish [en];\nGerman [de];\nTurkish [tr];', color=discord.Color.red())
        embed.set_author(
            name="Translate", icon_url="https://assets.tes.com/magazine-attachments/s3fs-public/styles/article_image_mobile/public/media/image/archived/teacher_cat.jpg?itok=-XzA4-SL")
        embed.set_footer(
            text="Made by the incredibly smart and talented Beyza with the help of hashymashy :)")
        # Send the embed.
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
