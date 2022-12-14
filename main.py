from nextcord.ext import commands, tasks
from itertools import cycle
import nextcord
import os

description = "A bot dedicated to Area-51."

intents = nextcord.Intents.default()
intents.message_content = True

status = cycle([
    "b!help for commands", "HARDCORE SEX", "TSFT Leaked Videos",
    "HENTAI SIMULATOR"
])

bot = commands.Bot(command_prefix="b!",
                   description=description,
                   intents=intents)

testServerId = 698021111304159252


@tasks.loop(minutes=20)
async def change_status():
    await bot.change_presence(activity=nextcord.Game(next(status)))


@bot.event
async def on_ready():
    change_status.start()
    print(f"{bot.user.name} is online!")


for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        bot.load_extension(f"cogs.{fn[:-3]}")


@bot.command(name="loadall")
@commands.has_permissions(administrator=True)
async def loadall(ctx):
    "Loads all cogs"
    counter = 0
    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{fn[:-3]}")
                counter += 1
            except commands.ExtensionAlreadyLoaded:
                pass
    if counter == 0:
        await ctx.send("All cogs are loaded already.")
    else:
        await ctx.send("Loaded all cogs!")


@loadall.error
async def loadall_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the permissions to use this command.")


@bot.command(name="unloadall")
@commands.has_permissions(administrator=True)
async def unloadall(ctx):
    "Unloads all cogs"
    counter = 0
    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            try:
                bot.unload_extension(f"cogs.{fn[:-3]}")
                counter += 1
            except commands.ExtensionNotLoaded:
                pass
    if counter == 0:
        await ctx.send("All cogs are unloaded already.")
    else:
        await ctx.send("Unloaded all cogs!")


@unloadall.error
async def unloadall_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the permissions to use this command.")


@bot.command(name="reloadall")
@commands.has_permissions(administrator=True)
async def reloadall(ctx):
    "Reloads all active cogs"
    for fn in os.listdir("./cogs"):
        if fn.endswith(".py"):
            try:
                bot.reload_extension(f"cogs.{fn[:-3]}")
            except commands.ExtensionNotLoaded:
                pass
    await ctx.send("All active cogs are reloaded.")


@reloadall.error
async def reloadall_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the permissions to use this command.")


@bot.command(name="load")
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    "Loads a cog"
    try:
        bot.load_extension(f"cogs.{extension}")
        await ctx.send("Loaded cog!")
    except commands.ExtensionAlreadyLoaded:
        await ctx.send("Cog already loaded.")
    except commands.ExtensionNotFound:
        await ctx.send("Cog not found.")


@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the permissions to use this command.")


@bot.command(name="unload")
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    "Unloads a cog"
    try:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send("Unloaded cog!")
    except commands.ExtensionNotLoaded:
        await ctx.send("Cog does not exist.")


@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the permissions to use this command.")


@bot.command(name="reload")
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    "Reloads a cog"
    try:
        bot.reload_extension(f"cogs.{extension}")
        await ctx.send("Reloaded cog!")
    except commands.ExtensionNotLoaded:
        await ctx.send("Cog does not exist.")


@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the permissions to use this command.")


if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])
