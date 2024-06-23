import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
llm = model()

@client.event
async def on_ready():
	print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startwith("ping"):
		await message.channel.send("pong")



@bot.command()
async def start(ctx, arg):
	await ctx.send(f"Hello the command is activited, the arg is {arg}")
	pass


@bot.command()
async def talk(ctx, arg):
	if llm == None:
		await ctx.send("You have not started the game yet")
	else:
		output = llm.generate_scenes(ctx.author.name, ctx.message.content)
		await ctx.send(output)
client.run(os.getenv("TOKEN"))
