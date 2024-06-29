import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from model import model

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
llm = model()


starter = open("prompt/starter.txt").read()

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith("ping"):
		await message.channel.send("pong")
		return
	if message.content.startswith("!start"):
		await message.channel.send(starter)
	if message.content.startswith("!t"):
		output = llm.generate_scenes(message.author.name, message.content)
		await message.channel.send(output)
	

client.run(os.getenv("TOKEN"))
