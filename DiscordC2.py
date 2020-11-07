import discord
from private.information import bot_token as TOKEN
from commands.commands import commands

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.split()[0] in commands:
        await message.channel.send(commands[message.content.split()[0]](message))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

client.run(TOKEN)
