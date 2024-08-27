import nextcord
from nextcord.ext import commands
from nextcord import Intents

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="activate the discord develloper badge")
async def badge(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

bot.run('')

