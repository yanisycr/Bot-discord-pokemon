import discord
import asyncio
from pokemon import *

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True  
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot connecté en tant que {client.user}')

def handle_user_messages(msg) -> str:
    message = msg.lower()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    user_message = message.content.lower()
    botfeedback = handle_user_messages(user_message)
    if botfeedback:
        await message.channel.send(botfeedback)

    if message.content.startswith('!pokemon'):
        user_message = message.content

        pokemon_message = await message.channel.send(trad_pokemon(user_message[9:]))


    if message.content.lower() == "bob":
        gif_url = 'https://tenor.com/view/spongebob-get-real-spongebob-get-real-spongebob-face-spongebob-ugly-gif-13309562138513808785'
        await message.channel.send(gif_url)

def runBot():
    discord_token = 'Mettre le toker du bot discord' 
    client.run(discord_token)

if __name__ == "__main__":
    runBot()
