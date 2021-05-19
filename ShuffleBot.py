import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.content) == "!Shuffle":
        await sendmsg(message, message.author.display_name, 1)

async def sendmsg(message, msg, num):
    await message.author.edit(nick=msg[0:num])
    num+=1
    if msg[0:num+1][-1] != ' ':
        time.sleep(0.5)
    if num > len(msg): num = 1
    await sendmsg(message,msg,num)

with open('creds.txt') as file:
    token = file.readlines()[0].rstrip('\n')

client.run(token)