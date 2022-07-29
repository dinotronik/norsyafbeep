from nextcord.ext import commands
import json, random, datetime, asyncio
import nextcord
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

repeating_show = random.choice(show)
repeating_action = random.choice(continuous_action)

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="b!", intents=intents)

@bot.command(name="fuckhadi")
async def SendMessage(ctx):
    await ctx.send('Fuck Hadi')


@bot.command(name="hadie")
async def hadie(ctx):
    await ctx.send("https://imgur.com/a/DwsTPm1")     

async def schedule_hourly_message(h, m, s, msg, channelid):
    while True:
        now = datetime.datetime.now()
        then = now.replace(hour=h, minute=m, second=s)
        if then < now:
            then += datetime.timedelta(seconds=1)
        wait_time = (then-now).total_seconds()
        await asyncio.sleep(wait_time)

        channel = bot.get_channel(channelid)

        await channel.send(msg)
        await asyncio.sleep(60*60)
        #change asyncio.sleep value to desired interval (in seconds)

@bot.command(name="hourly")
async def hourly(ctx, mystr:str, hour:int, minute:int, second:int):
    print(mystr, hour, minute, second)

    if not (0 < hour < 24 and 0 <= minute <= 60 and 0 <= second < 60):
        raise commands.BadArgument()

    time = datetime.time(hour, minute, second)
    timestr = time.strftime("%I:%M:%S %p")
    await ctx.send(f"An hourly message will be sent starting from {timestr} in this channel.\nHourly message: \"{mystr}\"\nConfirm by simply saying: `yes`")
    try:
        msg = await bot.wait_for("message", timeout=60, check=lambda message: message.author == ctx.author)
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond!")
        return

    if msg.content == "yes":
        await ctx.send("Hourly message is ready!")
        await schedule_hourly_message(hour, minute, second, mystr, ctx.channel.id)
    else:
        await ctx.send("Hourly message cancelled.")

async def hourly_shitpost(channelid):
    while datetime.datetime.now().minute == 0 and datetime.datetime.now().second == 0:
        five_man_list = random.sample(person, k=5)
        five_adj_list = random.sample(adjective, k=5)
        channel = bot.get_channel(channelid)
        global actions
        actions = [
            f"{random.choice(person)} has been sent to jail for {random.choice(continuous_action)}.",
            f"{random.choice(person)} has been sent to jail for being {random.choice(adjective)}.",
            f"{random.choice(person)} killed {random.choice(person)} with {random.choice(weapon)}.",
            f"{random.choice(person)} filed a lawsuit against {random.choice(person)}!",
            f"{random.choice(person)} filed a restraining order against {random.choice(person)}!",
            f"{random.choice(person)} blew up {random.choice(country)}! :tada:",
            f"{random.choice(country)} has declared a war against {random.choice(country)}! :crossed_swords:",
            f"{random.choice(person)} has become {random.choice(job)}!",
            f"BREAKING NEWS: {(repeating_action)[0].upper() + (repeating_action)[1:]} is now legal in {random.choice(country)}!",
            f"BREAKING NEWS: {(repeating_action)[0].upper() + (repeating_action)[1:]} is now illegal in {random.choice(country)}!",
            f"This just in—being {random.choice(adjective)} is now legal in {random.choice(country)}!",
            f"This just in—being {random.choice(adjective)} is now illegal in {random.choice(country)}!",
            f"{random.choice(person)} is now added to {random.choice(game)}!",
            f"{random.choice(show)} is adding a new character, its {random.choice(person)}!",
            f"Would you get locked in a room with {five_man_list[0]}, {five_man_list[1]} and {five_man_list[2]} for 5 million dollars?",
            f"{random.choice(person)} failed art school.",
            f"{random.choice(person)} has joined {random.choice(band)}!",
            f"{random.choice(person)} is now the leader of the \"{(repeating_action)[0].upper() + (repeating_action)[1:]}\" club.",
            f"{random.choice(person)} is now the leader of the \"Being {random.choice(adjective)}\" club.",
            f"Marvel had just announced a new superhero starring {random.choice(person)} in the MCU.",
            f"{random.choice(person)} has been caught {random.choice(continuous_action_with_noun)} {random.choice(person)}.",
            f"{random.choice(person)} was sent to hell for {random.choice(continuous_action)}. :smiling_imp:",
            f"{random.choice(person)} was sent to hell for being {random.choice(adjective)}. :smiling_imp:",
            f"If {random.choice(person)} was caught for {random.choice(continuous_action)}, they would probably {random.choice(verb_action)}.",
            f"{five_man_list[0]} x {five_man_list[1]} is now canon. :pleading_face::Happy_heart_wink::smiling_face_with_3_hearts:",
            f"{five_man_list[0]}, {five_man_list[1]} and {five_man_list[2]} are having a threesome. :hot_face::fire:",
            f"{random.choice(person)} was the imposter.",
            f"{random.choice(person)} was not the imposter.",
            f"{random.choice(person)} is featured in the next Star Wars film franchise.",
            f"Video Idea: \"DO NOT CALL {random.choice(person).upper()} FROM {(random.choice(game)).upper()} AT 3AM :scream::scream::skull:!! (SCARY)\"",
            f"Becoming {random.choice(job)} would definitely be a suitable job for {random.choice(person)}.",
            f"Becoming {random.choice(job)} would definitely not be a suitable job for {random.choice(person)}.",
            f"{random.choice(person)} took the L. :skull:",
            f"{random.choice(person)} is really good at {random.choice(game)}.",
            f"{random.choice(person)} is horrible at {random.choice(game)}.",
            f"{random.choice(person)} is really good at {random.choice(subject)}.",
            f"{random.choice(person)} is horrible at {random.choice(subject)}.",
            f"UPDATE: {random.choice(person)} got cancelled for {random.choice(continuous_action)}.",
            f"UPDATE: {random.choice(person)} got cancelled for being {random.choice(adjective)}.",
            f"{five_man_list[0]}, {five_man_list[1]} and {five_man_list[2]} walk into a bar...",
            f"Rejoice, {random.choice(person)} has become the new president of {random.choice(country)}! :crown:",
            f"Do not search \"{random.choice(person)} {random.choice(continuous_action)}\", biggest mistake of my life.",
            f"{random.choice(celebrity)} has hired {random.choice(person)}!",
            f"{random.choice(person)} is playing {random.choice(person)}'s mother.",
            f"Oh no, {random.choice(person)} and {random.choice(person)} are having an affair! :broken_heart:",
            f"Hear me out: {five_man_list[0]}, {five_man_list[1]} and {five_man_list[2]} in a movie directed by {random.choice(celebrity)}.",
            f"I wonder what {random.choice(person)} smells like. :nose: :triumph: :nose:",
            f"I can\'t hold it in anymore, I\'m gonna {random.choice(verb_action)}!",
            f"When life gives {random.choice(person)} lemons, they {random.choice(verb_action)}! :lemon:",
            f"{random.choice(person)} would be fun at parties.",
            f"What if {five_man_list[0]} and {five_man_list[1]} kissed {random.choice(place)} :open_mouth::flushed::heart_eyes:",
            f"Therapist: Don\'t worry, {random.choice(job).partition(' ')[2]} {random.choice(person)} isn\'t real, they cant hurt you.",
            f"This is so sad, {random.choice(person)} is {random.choice(adjective)}?",
            f"Who lives in a pineapple {random.choice(place)}? It was {random.choice(person)}. :pineapple:",
            f"{random.choice(person)} has converted to Muslim. Alhamdulillah my brothers! :kaaba:",
            f"{random.choice(person)} has converted to Christian. Amen! :cross:",
            f"{random.choice(person)} has converted to Buddhist. 阿弥陀佛! :pray:",
            f"The sister group for {random.choice(group)} consists of {five_man_list[0]}, {five_man_list[1]}, {five_man_list[2]}, {five_man_list[3]} and {five_man_list[4]}",
            f"A new season of {random.choice(show)} had just been announced starring {five_man_list[0]} and {five_man_list[1]}!",
            f"{random.choice(person)} just joined {random.choice(group)}:bangbang::bangbang:",
            f"Cluedo on crack: \"I suspect {random.choice(person)}, {random.choice(place)}, with {random.choice(weapon)}.\"",
            f"{random.choice(person)} is actually {random.choice(celebrity)}\'s long lost sibling.",
            f"{random.choice(person)} did a little trolling.",
            f"Today is {random.choice(person)}\'s birthday! :balloon::partying_face::tada:",
            f"Knock knock, {random.choice(person)}\'s on your door. Would you let them in?",
            f"{random.choice(person)} went back in time and {random.choice(past_action_with_noun)} {random.choice(person)}.",
            f"{random.choice(person)} went back in time to stop themselves from {random.choice(continuous_action)}.",
            f"{random.choice(person)} had just {random.choice(past_action_with_noun)} {random.choice(person)}. Cry about it.",
            f"Guys, being {random.choice(adjective)} is no laughing matter.",
            f"{random.choice(person)} is now transgender!",
            f"Describe {random.choice(person)} in 3 words: {five_adj_list[0]}, {five_adj_list[1]} and {five_adj_list[2]}",
            f"{random.choice(person)} is a {random.choice(celebrity)} fan.",
            f"{random.choice(person)} is a {random.choice(band)} stan.",
            f"It is better to {random.choice(verb_action)} {random.choice(place)} than to {random.choice(verb_action)} {random.choice(place)}.\n-{random.choice(person)}",
            f"{random.choice(person)} has adopted {random.choice(person)}.",
        ]
        shitpost_content = random.choice(actions)
        await channel.send(shitpost_content)
        await asyncio.sleep(1)
            

@bot.command(name="shitpost")
async def shitpost(ctx):
    await ctx.send("Hourly shitposting has commenced.")
    await hourly_shitpost(ctx.channel.id)

@hourly.error
async def hourly_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("""Incorrect format. Correct format: `b!hourly "[message]" [hour] [minute] [second]`""")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")

if __name__ == '__main__':
    bot.run(os.environ["DISCORD_TOKEN"])