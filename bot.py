from re import M
from nextcord.ext import commands
import json, random, datetime, asyncio
import nextcord
from nextcord import Interaction
import os

things = json.load(open("list.json"))

person = things['person']
continuous_action = things['continuous_action']
continuous_action_with_noun = things['continuous_action_with_noun']
past_action_with_noun = things['past_action_with_noun']
verb_action = things['verb_action']
adjective = things['adjective']
weapon = things['weapon']
country = things['country']
job = things['job']
game = things['game']
show = things['show']
band = things['band']
subject = things['subject']
celebrity = things['celebrity']
place = things['place']
group = things['group']

repeating_action = random.choice(continuous_action)

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

async def schedule_hourly_message(m, s, msg, channelid):
    while True:
        now = datetime.datetime.now()
        then = now.replace(hour=datetime.datetime.now().hour, minute=m, second=s)
        while then < now:
            then += datetime.timedelta(hours=1)
        wait_time = (then-now).total_seconds()
        await asyncio.sleep(wait_time)

        channel = bot.get_channel(channelid)

        await channel.send(msg)
        await asyncio.sleep(1)

@bot.slash_command(name="hourly", description="Sends an hourly message at a specific time.", guild_ids=[testServerId])
async def hourly(interaction: Interaction, message:str, minute:int, second:int):
    print(message, minute, second)

    if not (0 <= minute <= 60 and 0 <= second < 60):
        raise commands.BadArgument()
    
    hour = datetime.datetime.now().hour
    time = datetime.time(hour, minute, second)
    timemin = time.strftime("%-M")
    timesec = time.strftime("%-S")
    await interaction.response.send_message(f"An hourly message will be sent at every {timemin} minute and {timesec} second in this channel.\nHourly message: \"{message}\"")
    await schedule_hourly_message(minute, second, message, interaction.channel_id)

@bot.command(name="hourly")
async def hourly(ctx, message:str, minute:int, second:int):
    print(message, minute, second)

    if not (0 <= minute <= 60 and 0 <= second < 60):
        raise commands.BadArgument()

    hour = datetime.datetime.now().hour
    time = datetime.time(hour, minute, second)
    timemin = time.strftime("%-M")
    timesec = time.strftime("%-S")
    await ctx.send(f"An hourly message will be sent at every {timemin} minute and {timesec} second in this channel.\nHourly message: \"{message}\"\nTo confirm simply type `yes`")
    try:
        msg = await bot.wait_for("message", timeout=60, check=lambda message: message.author == ctx.author)
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond!")
        return

    if msg.content == "yes":
        await ctx.send("Hourly message is ready!")
        await schedule_hourly_message(minute, second, message, ctx.channel.id)
    else:
        await ctx.send("Hourly message cancelled.")

@hourly.error
async def hourly_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("""Incorrect format. Correct format: `b!hourly "[message]" [minute] [second]`""")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")

if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])