import re
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from model import Gemini

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
llm = Gemini()


starter = open("prompt/starter.txt").read()

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")


characters = {}

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith("ping"):
		await message.channel.send("pong")
		return
	if message.content.startswith("!start"):
		respond_message = open("prompt/character_remember.txt").read()
		await message.channel.send(respond_message)

	if message.content.startswith("!add"):
		content = open("prompt/character_remember_user.txt").read()
		character_name = re.search('Character Name:.(\w+)', message.content).group(1)
		print(character_name)
		discord_name = re.search('Discord Name:.(\w+)', message.content).group(1)
		backstory = re.search('Character Backstory:.(\w+)', message.content).group(1)
		class_input = re.search('Class:.(\w+)', message.content).group(1)
		alignment = re.search('Alignment:.(\w+)', message.content).group(1)
		
		characters[discord_name] = character_name

		content = content.replace("{{CHARACTER_NAME}}", character_name)
		content = content.replace("{{DISCORD_NAME}}",discord_name)
		content = content.replace("{{BACKGROUND}}",backstory)
		content = content.replace("{{CLASS}}",class_input)
		content = content.replace("{{ALIGNMENT}}", alignment)
		result = llm.asscoicate_characters(content)
		await message.channel.send(result)

	if message.content.startswith("!t"):
		character_name = characters.get(message.author.name, message.author.name)
		output = llm.generate_scenes(message.author.name, message.content)
		await message.channel.send(output)
	

client.run(os.getenv("TOKEN"))
