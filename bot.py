from re import M
from nextcord.ext import commands
import nextcord
from nextcord import Interaction
import os

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="b!", intents=intents)
testServerId = 698021111304159252

@bot.slash_command(name="say", description="Repeats your message.", guild_ids=[testServerId])
async def sendmessage(interaction: Interaction, message):
    if interaction.user.id == 234258656911163392:
        await interaction.response.send_message("Syaffique is fucking stupid.")
    else:
        await interaction.response.send_message(message)

@bot.command(name="say")
async def SendMessage(ctx, message:str):
    if ctx.author.id == 234258656911163392:
        await ctx.send("Syaffique is fucking stupid.")
    else:
        await ctx.send(message)

@bot.slash_command(name="hadie", description="Sends a picture of Hadi, Professional Mother Player.", guild_ids=[testServerId])
async def hadie(interaction: Interaction):
    await interaction.response.send_message("https://imgur.com/OlwPF6S")

@bot.command(name="hadie")
async def hadie(ctx):
    await ctx.send("https://imgur.com/OlwPF6S")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")

if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])