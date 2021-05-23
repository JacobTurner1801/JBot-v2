import discord
from googlesearch import search
TOKEN = open("token.txt", "r").read()
SERVER_ID = 394868206545797130

client = discord.Client()
commands_usable = """```py
def commands():
    YEE = usable
    X = not usable
    ADMIN = only Jacob
    return {
        YEE - !commands: 'returns the commands'
        YEE - !hello: 'says hello'
        YEE - !search: 'googles what you put after'
        ADMIN - !logout: 'disconnects the bot'
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
    if check_command("!commands", m):
        await message.channel.send(commands_usable)
    elif check_command("!hello", m):
        await message.channel.send("Hello")
    elif check_command("!search", m):
        res = await google_search(m)
        for i in range(len(res)):
            await message.channel.send(str(res[i]))
    elif check_command("!logout", m):
        await message.channel.send("Bye then")
        await client.close()
        if not check_command("!logout", m):
            await message.channel.send("Only Jacob can close me down!")
# end return_message


async def google_search(message) -> list:
    m = message.split()
    query = m[1]  # get the query to google
    res = []
    for i in search(query=query, num=5, start=0, stop=10, pause=1):  # shows first 5 results
        res.append(i)
    return res


def check_command(command, m) -> bool:
    if command == m or command in m:
        return True
    else:
        return False
# end check_command


client.run(TOKEN)
