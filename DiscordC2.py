import discord
from private.information import bot_token as TOKEN
from commands.commands import commands

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.split()[0].lower() in commands:
        result = await commands[message.content.split()[0]](message)
        if result != '' and result is not None:
            await message.channel.send(result)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

client.run(TOKEN)
