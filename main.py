import discord

SECRET_TOKEN_PATH = "token.txt"

client = discord.Client()

def get_secret_token(filename):
    file = open(filename, "r+")
    return file.readline()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print("{}: {}".format(message.author, message.content))
    if message.author == client.user:
        return

    if message.content.startswith('/phallus'):
        await message.channel.send('Omer has the biggest phallus in the chat.')

def __init__():
    client.run(get_secret_token(SECRET_TOKEN_PATH))

__init__()
