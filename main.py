import os
import discord
import random
from discord.ext import commands

TOKEN = os.environ['Token']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="*", intents=intents)

@bot.command(name="d4")
async def rolld4(ctx):
  d4 = random.randint(1, 4)
  await ctx.channel.send(f"Rolling a d4: {d4}")

@bot.command(name="d6")
async def rolld6(ctx):
  d6 = random.randint(1, 6)
  await ctx.channel.send(f"Rolling a d6: {d6}")

@bot.command(name="d8")
async def rolld8(ctx):
  d8 = random.randint(1, 8)
  await ctx.channel.send(f"Rolling a d8: {d8}")

@bot.command(name="d10")
async def rolld10(ctx):
  d10 = random.randint(1, 10)
  await ctx.channel.send(f"Rolling a d10: {d10}")

@bot.command(name="d12")
async def rolld12(ctx):
  d12 = random.randint(1, 12)
  await ctx.channel.send(f"Rolling a d12: {d12}")

@bot.command(name="d20")
async def rolld20(ctx):
  d20 = random.randint(1, 20)
  await ctx.channel.send(f"Rolling a d20: {d20}")

@bot.command(name="d100")
async def rolld100(ctx):
  d100 = random.randint(1, 100)
  await ctx.channel.send(f"Rolling a d100: {d100}")

@bot.command(name="roll")
async def roll(ctx,*args):
  args = list(args)
  print(args)
  for i in range(len(args)):
    if "," not in args[i]:
      args[i] = args[i] + ",1"
    print(args[i].split(","))
    print(args[0])
    dice_number = args[i] + args[i+1]
    await ctx.channel.send(dice_number)

@bot.command(name = "tavern")
async def tavern(ctx):
  tavernmusic = "[Tavern Music](https://www.youtube.com/watch?v=EULoybB2Nsw)."
  await ctx.channel.send(tavernmusic)

@bot.command(name = "travel")
async def travel(ctx):
  travelmusic = "[Travel Music](https://www.youtube.com/watch?v=A8qMyBWZNw0)."
  await ctx.channel.send(travelmusic)

@bot.command(name = "battle")
async def battle(ctx):
  battlemusic = "[Battle Music](https://www.youtube.com/watch?v=A48QqpWKWG8)."
  await ctx.channel.send(battlemusic)

@bot.command(name = "ambient")
async def ambient(ctx):
  ambientmusic = "[Ambient Music](https://www.youtube.com/watch?v=CahOLfYxiq0)."
  await ctx.channel.send(ambientmusic)





bot.run(TOKEN)