import discord
import time
from discord.ext import tasks

client = discord.Client()

inputs = {}
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@tasks.loop(seconds=0.8)
async def my_background_task():
    for name,status in inputs.items():
        num = status[0]
        await status[1].edit(nick=status[2][0:num])
        num+=1
        if num > len(status[2]): num = 1
        if name in inputs.keys():
            inputs[name] = [num, status[1], status[2]]
        
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.content) == "!Shuffle":
        inputs[message.author.id] = [1, message.author, message.author.display_name]
        if my_background_task.is_running():
            pass
        else: my_background_task.start()

    if str(message.content) == "!Shtop":
        try:
            del inputs[message.author.id]
        except:
            pass

with open('creds.txt') as file:
    token = file.readlines()[0].rstrip('\n')

client.run(token)


