from nextcord.ext import commands
import nextcord
from gtts import gTTS

testServerId = 698021111304159252


class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join')
    async def join(self, ctx):
        "Join a voice channel"
        user = ctx.message.author
        if user.voice != None:
            try:
                await user.voice.channel.connect()
            except:
                await ctx.send("I am already in a voice channel.")
        else:
            await ctx.send(
                "You need to be in a voice channel to run this command.")

    @commands.command(name="leave")
    async def leave(self, ctx):
        "Leave a voice channel"
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
        else:
            await ctx.send("I am not in a voice channel.")

    @commands.command(name="tts")
    async def tts(self, ctx, *args):
        "Sends a Text-to-Speech message in a voice channel"
        text = " ".join(args)
        user = ctx.message.author
        if user.voice != None:
            try:
                vc = await user.voice.channel.connect()
            except:
                vc = ctx.voice_client
            if vc.is_playing():
                vc.stop()

            myobj = gTTS(text=text, lang="en", slow=False)
            myobj.save("tts-audio.mp3")

            source = await nextcord.FFmpegOpusAudio.from_probe(
                "tts-audio.mp3", method='fallback')
            vc.play(source)
        else:
            await ctx.send(
                'You need to be in a voice channel to run this command!')


def setup(bot):
    bot.add_cog(Voice(bot))
