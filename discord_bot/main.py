import dis_settings
import discord
from discord.ext import commands
from discord.ext.commands.context import Context

import os
import asyncio





#DJANGO SETUP
from pathlib import Path
import sys
from django import setup

path = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
setup()

# DJANGO IMPORTS
from discord_bot.models import MuteRole

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Success: Bot is connected to discord")

@bot.event
async def on_guild_join(guild:discord.guild.Guild):
    print("trigred on_guild_join")
    print(f"Guild roles:{guild.roles}")
    mute_role_obj:MuteRole =  MuteRole.objects.create(guild_id=str(guild.id))

@bot.event
async def on_command_error(ctx:Context,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Error : missing required arguments.are you sure u provided all the arguments?")

    elif isinstance(error,commands.MissingPermissions):
        await ctx.send("Error : missing required permissions.are you suer u have all the permissions?")

    else:
        await(ctx.send(f"Error:{error} accured with type {type(error)}"))
    

            
@bot.event
async def on_guild_remove(guild):
    print("trigred on_guild_remove")
    mute_role_obj:MuteRole =  MuteRole.objects.get(guild_id=str(guild.id))
    mute_role_obj.delete()

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(dis_settings.DISCORD_API_SECRET)



asyncio.run(main())

