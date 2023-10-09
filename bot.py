import discord
import responses
import youtube_dl
import os
import signal

class MyBot(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.voice_client = None

    async def on_ready(self):
        print(f'{self.user} is now running!')

    async def on_message(self, message):
        if self.user != message.author:
            if message.content == '!samsung-notification' and (message.author.voice and message.author.voice.channel):
                voice_channel = message.author.voice.channel
                if not self.voice_client:
                    self.voice_client = await voice_channel.connect()
                    self.voice_client.play(discord.FFmpegPCMAudio(
                        executable=r"C:\Users\HP\source\repos\DiscordBot\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe",
                        source=r"C:\Users\HP\source\repos\DiscordBot\X2Download.app - Samsung notification sound (128 kbps).mp3"
                    ))
                else:
                    self.voice_client.play(discord.FFmpegPCMAudio(
                        executable=r"C:\Users\HP\source\repos\DiscordBot\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe",
                        source=r"C:\Users\HP\source\repos\DiscordBot\X2Download.app - Samsung notification sound (128 kbps).mp3"
                    ))

            if message.content[0:5:1] == '!play' and (message.author.voice and message.author.voice.channel):
                url = message.content[6::1]
                voice_channel = message.author.voice.channel

                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    url2 = info['formats'][0]['url']

                if self.voice_client == None:
                    self.voice_client = await voice_channel.connect()
                    self.voice_client.stop()
                    self.voice_client.cleanup()
                    self.voice_client.play(discord.FFmpegPCMAudio(
                        executable=r"C:\Users\HP\source\repos\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe",
                        source=url2))
                else:
                    self.voice_client.stop()
                    self.voice_client.cleanup()
                    self.voice_client.play(discord.FFmpegPCMAudio(
                        executable=r"C:\Users\HP\source\repos\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe",
                        source=url2))

            if message.content == '!stop' and self.voice_client != None:
                await self.voice_client.disconnect()
                self.voice_client = None

            if message.content == '!pause' and self.voice_client != None:
                self.voice_client.pause()

            if message.content == '!resume' and self.voice_client != None:
                self.voice_client.resume()

            if message.content[0] == '!' and message.content[0:5:1] != '!play':
                response = responses.usual_responses(message.content)
                await message.channel.send(response)
                print(f"user:{message.author} sent: '{message.content}' to channel '{message.channel}'")

    async def on_voice_state_update(self, member, before, after):
        if member == self.user:
            if before.channel and not after.channel:
                self.voice_client = None