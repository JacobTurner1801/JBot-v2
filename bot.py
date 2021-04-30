import discord
from discord.ext import commands
import os
TOKEN = open("token.txt", "r").read()
SERVER_ID = 394868206545797130

client = discord.Client()

commands_usable = """```py
def commands():
    YEE = usable
    X = not usable
    ADMIN = only Jacob
    return {
        YEE - jbot.commands(): 'returns the commands'
        YEE - jbot.hello(): 'says hello'
        ADMIN - jbot.logout(): 'disconnects the bot'
        X - jbot.search(): 'googles what you put after'
    } ```"""


@client.event
async def on_ready():
    print(f"we have logged in as {client.user} ")
    await client.change_presence(status=discord.Status.online)


@client.event
async def on_message(message):
    guild = client.get_guild(SERVER_ID)
    author_roles = message.author.roles
    await return_message(message)
# end on_message


async def return_message(message):
    m = message.content.lower()
    if check_command("jbot.commands()", m):
        await message.channel.send(commands_usable)
    elif check_command("jbot.hello()", m):
        await message.channel.send("Hello")
    elif check_command("jbot.logout()", m):
        await message.channel.send("Bye then")
        await client.close()
    elif not check_command("jbot.logout()", m):
        await message.channel.send("Only Jacob can close me down!")
# end return_message


def check_command(command, m):
    if command == m:
        return True
    else:
        return False
# end check_command


client.run(TOKEN)
