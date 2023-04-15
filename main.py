from discord_bot import DiscordBot
from get_paper import get_papers

DISCORD_BOT_TOKEN = 'Discordボットのトークンを入力してください。'
DISCORD_CHANNEL_ID = 1234567890  # 投稿したいチャンネルIDを入力

papers = get_papers()
bot = DiscordBot(DISCORD_BOT_TOKEN, DISCORD_CHANNEL_ID, papers)
bot.run(DISCORD_BOT_TOKEN)
