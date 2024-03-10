import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import json

#DJANGO SETUP
import os
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
from discord_bot.models import MuteRole

class Mute(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"mute cog is online.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setmuterole(self,ctx:Context,role:discord.Role):
        print("SETMUTEROLE Command trigerd!!!")
        mute_role_obj:MuteRole = MuteRole.objects.get(guild_id = str(ctx.guild.id))
        
        mute_role_obj.role_id = role.id
        mute_role_obj.save()

        conf_embed = discord.Embed(
             title="success!",
             color=discord.Color.green()
        )
        conf_embed.add_field(
            name="Mute role has been set!",
            value=f"The mute role has been changed to '{role.mention}' for this guild. all members who are muted will be equipped with this role.",
            inline=False
        )
        await ctx.send(embed=conf_embed)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self,ctx:Context,member:discord.Member):
        print("MUTE Command trigerd!!!")
        mute_role_obj:MuteRole =MuteRole.objects.get(guild_id = str(ctx.guild.id))
        mute_role_id = mute_role_obj.role_id
        if not mute_role_id:
            conf_embed = discord.Embed(
                title="Failed!",
                color=discord.Color.green()
            )
            conf_embed.add_field(
                name="Failed!",
                value=f"No Mute role set for mute!Make sure to set the mute role using <setmuterole> bot command.",
                inline=False
            )
            await ctx.send(embed=conf_embed)

        mute_role = discord.utils.get(ctx.guild.roles, id=int(mute_role_id))
        print(mute_role)
        print(f'Member passed {member.name} with {member.id}.')
        
        if mute_role not in member.roles:
            print("Condition meat! ")
            await member.add_roles(mute_role)
            conf_embed = discord.Embed(
                title="success!",
                color=discord.Color.green()
            )
            conf_embed.add_field(
                name="Muted!",
                value=f"{member.mention} has been muted by {ctx.author.mention}",
                inline=False
            )
            await ctx.send(embed=conf_embed)
        else:
            conf_embed = discord.Embed(
                title="Failed!",
                color=discord.Color.green()
            )
            conf_embed.add_field(
                name="Failed!",
                value=f"{member.mention} is already muted with {mute_role.mention}",
                inline=False
            )
            await ctx.send(embed=conf_embed)
        
            

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self,ctx:Context,member:discord.Member):
        print("UNMUTE Command trigerd!!!")
        mute_role_obj:MuteRole =MuteRole.objects.get(guild_id = str(ctx.guild.id))
        mute_role_id = mute_role_obj.role_id 
        mute_role = discord.utils.get(ctx.guild.roles, id=int(mute_role_id))
        print(type(mute_role))
        print(f"All permissions {ctx.permissions}!!!")
        if mute_role in member.roles:
            await member.remove_roles(mute_role)
            conf_embed = discord.Embed(
                title="success!",
                color=discord.Color.green()
            )
            conf_embed.add_field(
                name="Unmuted!",
                value=f"{member.mention} has been unmuted by {ctx.author.mention}",
                inline=False
            )
            await ctx.send(embed=conf_embed)
        else:
            conf_embed = discord.Embed(
                title="Failed!",
                color=discord.Color.green()
            )
            conf_embed.add_field(
                name="Failed!",
                value=f"{member.mention} is not muted with {mute_role.mention}",
                inline=False
            )
            await ctx.send(embed=conf_embed)

        
async def setup(bot):
    await bot.add_cog(Mute(bot))