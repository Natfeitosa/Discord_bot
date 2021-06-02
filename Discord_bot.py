import discord
import asyncio
import random
import requests
import json
from PIL import Image
from io import BytesIO
import os
import Types as T
import helper


disco_token = open("disco_key.json")
tk = json.load(disco_token)
TOKEN = tk["key"]
client = discord.Client()

@client.event
async def on_message(message):
    channel = message.channel
    #print(client.user())
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
#bot doesnt take kindly to foul language
    # if "fuck" in message.content.lower():#bot is constantly checking every message it recieves
    #     await channel.send("{.author} HEY WATCH YOUR F***IGN LANGUAGE".format(message))#code so it can reply or send message
    # elif "fck" in message.content.lower():
    #     await channel.send("{.author} HEY WATCH YOUR F***IGN LANGUAGE".format(message))
    # elif "fk" in message.content.lower():
    #     await channel.send("{.author} HEY WATCH YOUR F***IGN LANGUAGE".format(message))
    # elif "fucking" in message.content.lower():
    #     await channel.send("{.author} HEY WATCH YOUR F***IGN LANGUAGE".format(message))
    # elif "fking" in message.content.lower():
    #     await channel.send("{.author} HEY WATCH YOUR F***IGN LANGUAGE".format(message))



    if message.content.startswith('!hiragana'):
        await channel.send("What hiragana do you want to check?")

        def check_a(m):
            m.content=m.content.lower()
            print(m.content)
            return m.content == helper.Letter(m.content) and m.channel == channel#the bot waits for the reply and is looking for a spefic wording


        msg = await client.wait_for('message', check=check_a)
        msg.content=msg.content.lower()
        await channel.send(helper.Hira(msg.content).format(msg))#after it recieves the spefic word it was looking for this will fetch the corresponding hiragana and print it to the user

    if message.content.startswith('!katakana'):
        await channel.send("What katakana do you want to check?")

        def check_a(m):
            m.content=m.content.lower()
            print(helper.Letter(m.content))
            return m.content == helper.Letter(m.content) and m.channel == channel


        msg = await client.wait_for('message', check=check_a)
        print(msg.content)
        msg.content=msg.content.lower()
        await channel.send(helper.Katakana(msg.content).format(msg))


    if message.content.startswith("!poke"):
        await channel.send("What type do you want?")
        def check_a(m):
            return m.content==T.Types(m.content) and m.channel == channel

        msg = await client.wait_for('message',check=check_a)
        url="https://unpkg.com/pokemons@1.1.0/pokemons.json"
        pokedex = requests.get(url).json()
        pokemon = json.dumps(pokedex)
        temp_new_pokedex= pokemon[12:-1]
        new_pokedex=json.loads(temp_new_pokedex)
        found = False
        imagelink=""
        namep=""
        while(not(found)):
            poke = random.choice(new_pokedex)
            for type in poke["type"]:
                if(type == msg.content):
                    found = True
                    imagelink = poke["sprites"]["large"]
                    namep=poke["name"]
        url_request = requests.get(imagelink)
        if(url_request.status_code==200):
            process = BytesIO(url_request.content)
            img = Image.open(process)
            img.save(namep+".jpg")
            await channel.send(namep,file=discord.File(namep+".jpg"))
            delete_file = os.path.join(os.getcwd(),namep+".jpg")
            os.remove(delete_file)
        else:
            await channel.send("INVALID URL")

@client.event#we use this to turn on the bot
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
