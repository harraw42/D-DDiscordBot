import discord
import random
from discord.ext import commands

TOKEN = "MTA4MjA3MTcwMzQzMTE3MjE4Ng.Guo-sb.oADsSGCTc7OsYLQTmAYMGK4qHbmxtgbLrkFQ3A"

intents = discord.Intents.defaults()
intents.message_content = True

bot = commands.Bot(command_prefix = "*", intents = intents)

@bot.command(name = "roll d4")
async def rolld4(ctx):
  d4 = random.randint(1,4)
  await ctx.channel.send(f"Rolling a d4: {d4}")

@bot.command(name = "roll d6")
async def rolld6(ctx):
  d6 = random.randint(1,6)
  await ctx.channel.send(f"Rolling a d6: {d6}")

@bot.command(name = "roll d8")
async def rolld8(ctx):
  d8 = random.randint(1,8)
  await ctx.channel.send(f"Rolling a d8: {d8}")

@bot.command(name = "roll d10")
async def rolld10(ctx):
  d10 = random.randint(1,10)
  await ctx.channel.send(f"Rolling a d10: {d10}")

@bot.command(name = "roll d12")
async def rolld12(ctx):
  d12 = random.randint(1,12)
  await ctx.channel.send(f"Rolling a d12: {d12}")

@bot.command(name = "battle")
async def get_initiative(ctx):
  await ctx.channel.send("How many creatures in battle?")
















bot.run(TOKEN)