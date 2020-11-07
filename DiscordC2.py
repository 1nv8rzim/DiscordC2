import discord
from private.information import bot_token as TOKEN

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = f'Hello {message.author.mention}'
        await message.channel.send(msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

client.run(TOKEN)
