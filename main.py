# Import necessary modules
import os
import discord
import random
from discord.ext import commands

# Get bot token from environment variable
TOKEN = os.environ['Token']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="*", intents=intents)

@bot.command(name="commands")
async def commands(ctx):
  await ctx.channel.send"""
  ----- C O M M A N D S -----
  (Prefix a command with "*")

  *d4 - rolls a d4

  *d6 - rolls a d6

  *d8 - rolls a d8

  *d10 - rolls a d10

  *d12 - rolls a d12

  *d20 - rolls a d20

  *d100 - rolls a d100

  *roll {enter number of dice} d{enter type of dice} - rolls the requested number of the 
  requested dice

  *tavern - plays tavern music

  *battle - plays battle music

  *travel - plays travel music

  *ambience - plays ambient music
  """

#Define a command for rolling each singular die, with a send command to send "Rolling a {die}" then the result
#d4
@bot.command(name="d4")
async def rolld4(ctx):
  d4 = random.randint(1, 4)
  await ctx.channel.send(f"Rolling a d4: {d4}")

#d6
@bot.command(name="d6")
async def rolld6(ctx):
  d6 = random.randint(1, 6)
  await ctx.channel.send(f"Rolling a d6: {d6}")

#d8
@bot.command(name="d8")
async def rolld8(ctx):
  d8 = random.randint(1, 8)
  await ctx.channel.send(f"Rolling a d8: {d8}")

#d10
@bot.command(name="d10")
async def rolld10(ctx):
  d10 = random.randint(1, 10)
  await ctx.channel.send(f"Rolling a d10: {d10}")

#d12
@bot.command(name="d12")
async def rolld12(ctx):
  d12 = random.randint(1, 12)
  await ctx.channel.send(f"Rolling a d12: {d12}")

#d20
@bot.command(name="d20")
async def rolld20(ctx):
  d20 = random.randint(1, 20)
  await ctx.channel.send(f"Rolling a d20: {d20}")

#d100
@bot.command(name="d100")
async def rolld100(ctx):
  d100 = random.randint(1, 100)
  await ctx.channel.send(f"Rolling a d100: {d100}")

@bot.command(name="roll")
async def roll(ctx,*args):
  args = list(args)
  num = args[0]
  die = args[1]
  for i in range(len(num)):
    dice_total = int(num) * int(die[1:]) #string comprehension, gets rid of "d"
    dice_outcome = random.randint(1, dice_total)
    await ctx.channel.send(f"Rolling {num}{die}: {dice_outcome}")

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

@bot.command(name = "pregame")
async def pregame(ctx):
  pregamemusic = "[Pregame Music](https://www.youtube.com/watch?v=FFfdyV8gnWk)."
  await ctx.channel.send(pregamemusic)

bot.run(TOKEN)