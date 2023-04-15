import discord
from discord.ext import commands


class DiscordBot(commands.Bot):
    def __init__(self, token, channel_id, papers):
        self.token = token
        self.channel_id = channel_id
        self.papers = papers

        intents = discord.Intents.default()
        super().__init__(command_prefix='!', intents=intents)

    async def on_ready(self):
        print(f'We have logged in as {self.user}')
        await self.send_papers_on_ready()

    async def send_papers_on_ready(self):
        channel = self.get_channel(self.channel_id)
        await self.post_papers(channel)

    async def post_papers(self, channel):
        try:
            for paper in self.papers:
                await channel.send(paper)
        except Exception as e:
            print(f"Error posting papers: {e}")
