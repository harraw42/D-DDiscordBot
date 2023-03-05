import discord
import random
from discord.ext import commands

TOKEN = "6394d250b64f62260a0efa6b20b6b532d6854a525014e098afe056b9a5e33249"

intents = discord.Intents.defaults()
intents.message_content = True

client = commands.Bot(command_prefix = "!", intents = intents)

class initiative:
  