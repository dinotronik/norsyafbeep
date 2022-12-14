from nextcord.ext import tasks, commands
import json, random, datetime, asyncio

testServerId = 698021111304159252

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


class Shitpost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.printer.start()

    @tasks.loop(hours=24)
    async def printer(self):
        repeating_action = random.choice(continuous_action)
        five_man_list = random.sample(person, k=5)
        five_adj_list = random.sample(adjective, k=5)
        actions = [
            f"{random.choice(person)} has been sent to jail for {random.choice(continuous_action)}.",
            f"{random.choice(person)} has been sent to jail for being {random.choice(adjective)}.",
            f"{random.choice(person)} killed {random.choice(person)} with {random.choice(weapon)}.",
            f"{random.choice(person)} filed a lawsuit against {random.choice(person)}! :classical_building::judge:",
            f"{random.choice(person)} filed a restraining order against {random.choice(person)}! :notepad_spiral::negative_squared_cross_mark:",
            f"{random.choice(person)} blew up {random.choice(country)}! :tada:",
            f"{random.choice(country)} has declared a war against {random.choice(country)}! :crossed_swords:",
            f"{random.choice(person)} has become {random.choice(job)}!",
            f"BREAKING NEWS: {(repeating_action)[0].upper() + (repeating_action)[1:]} is now legal in {random.choice(country)}! :white_check_mark:",
            f"BREAKING NEWS: {(repeating_action)[0].upper() + (repeating_action)[1:]} is now illegal in {random.choice(country)}! :negative_squared_cross_mark:",
            f"This just in???being {random.choice(adjective)} is now legal in {random.choice(country)}! :white_check_mark:",
            f"This just in???being {random.choice(adjective)} is now illegal in {random.choice(country)}! :negative_squared_cross_mark:",
            f"{random.choice(person)} is now added to {random.choice(game)}!",
            f"{random.choice(show)} is adding a new character, its {random.choice(person)}!",
            f"Would you get locked in a room with {five_man_list[0]}, {five_man_list[1]} and {five_man_list[2]} for 5 million dollars?",
            f"{random.choice(person)} failed art school, this can't be good.",
            f"{random.choice(person)} has joined {random.choice(band)}!",
            f"{random.choice(person)} is now the leader of the \"{(repeating_action)[0].upper() + (repeating_action)[1:]}\" club.",
            f"{random.choice(person)} is now the leader of the \"Being {random.choice(adjective)}\" club.",
            f"Marvel had just announced a new superhero starring {random.choice(person)} in the MCU. :man_superhero:",
            f"{random.choice(person)} has been caught {random.choice(continuous_action_with_noun)} {random.choice(person)}.",
            f"{random.choice(person)} was sent to hell for {random.choice(continuous_action)}. :smiling_imp:",
            f"{random.choice(person)} was sent to hell for being {random.choice(adjective)}. :smiling_imp:",
            f"If {random.choice(person)} was caught for {random.choice(continuous_action)}, they would probably {random.choice(verb_action)}.",
            f"{five_man_list[0]} x {five_man_list[1]} is now canon. :pleading_face::heart_eyes::smiling_face_with_3_hearts:",
            f"{five_man_list[0]}, {five_man_list[1]} and {five_man_list[2]} are having a threesome. :hot_face::fire:",
            f"{random.choice(person)} was the imposter. :postbox:",
            f"{random.choice(person)} was not the imposter. :postbox:",
            f"{random.choice(person)} is featured in the next Star Wars film franchise. :star::crossed_swords:",
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
            f"Do not search {random.choice(person)} {random.choice(continuous_action)}, worst mistake of my life.",
            f"{random.choice(celebrity)} has hired {random.choice(person)}!",
            f"{random.choice(person)} is playing {random.choice(person)}'s mother.",
            f"Oh no, {random.choice(person)} and {random.choice(person)} are having an affair! :broken_heart:",
            f"Hear me out: {five_man_list[0]}, {five_man_list[1]} and {five_man_list[2]} in a movie directed by {random.choice(celebrity)}.",
            f"I wonder what {random.choice(person)} smells like. :nose: :triumph: :nose:",
            f"I can\'t hold it in anymore, I\'m gonna {random.choice(verb_action)}!",
            f"When life gives {random.choice(person)} lemons, they {random.choice(verb_action)}! :lemon:",
            f"{random.choice(person)} would be fun at parties. :tada:",
            f"What if {five_man_list[0]} and {five_man_list[1]} kissed {random.choice(place)} :open_mouth::flushed::heart_eyes:",
            f"Therapist: Don\'t worry, {random.choice(job).partition(' ')[2]} {random.choice(person)} isn\'t real, they cant hurt you.",
            f"{random.choice(person)} is {random.choice(adjective)}. This is so sad, Can we hit 15 likes? :cry:",
            f"Who lives in a pineapple {random.choice(place)}? It was {random.choice(person)}. :pineapple:",
            f"{random.choice(person)} has converted to Muslim. Alhamdulillah my brothers! :kaaba:",
            f"{random.choice(person)} has converted to Christian. Amen! :cross:",
            f"{random.choice(person)} has converted to Buddhist. ????????????! :pray:",
            f"The sister group for {random.choice(group)} consists of {five_man_list[0]}, {five_man_list[1]}, {five_man_list[2]}, {five_man_list[3]} and {five_man_list[4]}.",
            f"A new season of {random.choice(show)} had just been announced starring {five_man_list[0]} and {five_man_list[1]}!",
            f"{random.choice(person)} just joined {random.choice(group)}:bangbang::bangbang:",
            f"Cluedo on crack: \"I suspect {random.choice(person)}, {random.choice(place)}, with {random.choice(weapon)}.\"",
            f"{random.choice(person)} is actually {random.choice(celebrity)}\'s long lost sibling.",
            f"{random.choice(person)} did a little trolling. :smiling_imp:",
            f"Today is {random.choice(person)}\'s birthday! :balloon::partying_face::tada:",
            f"Knock knock, {random.choice(person)}\'s on your door. Will you let them in?",
            f"{random.choice(person)} went back in time and {random.choice(past_action_with_noun)} {random.choice(person)}.",
            f"{random.choice(person)} went back in time to stop themselves from {random.choice(continuous_action)}.",
            f"{random.choice(person)} has just {random.choice(past_action_with_noun)} {random.choice(person)}. Cry about it.",
            f"Guys, being {random.choice(adjective)} is no laughing matter.",
            f"{random.choice(person)} is now transgender! :transgender_flag:",
            f"Describe {random.choice(person)} in 3 words: {five_adj_list[0]}, {five_adj_list[1]} and {five_adj_list[2]}.",
            f"{random.choice(person)} is a {random.choice(celebrity)} fan.",
            f"{random.choice(person)} is a {random.choice(band)} stan.",
            f"It is better to {random.choice(verb_action)} {random.choice(place)} than to {random.choice(verb_action)} {random.choice(place)}.\n-{random.choice(person)}",
            f"{random.choice(person)} has adopted {random.choice(person)}.",
            f"I saw {random.choice(person)} {random.choice(continuous_action_with_noun)} {random.choice(person)}. :astonished:",
            f"I saw {random.choice(person)} {random.choice(continuous_action_with_noun)} children. Should I call the cops?",
            f"In a game of hide and seek, {random.choice(person)} would most likely hide {random.choice(place)}."
        ]
        now = datetime.datetime.now() - datetime.timedelta(hours=16)
        then = now.replace(hour=0, minute=0, second=0,
                           microsecond=0) + datetime.timedelta(days=1)
        wait_time = (then - now).total_seconds()
        if then > now:
            await asyncio.sleep(wait_time)
        channel_id = 1002088606904627250
        channel = self.bot.get_channel(channel_id)
        await channel.send(f"{random.choice(actions)}")


def setup(bot):
    bot.add_cog(Shitpost(bot))
