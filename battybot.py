import asyncio
import os

import aiohttp

import discord
from discord.ext import commands
from discord.ext.commands import CommandInvokeError
from discord.ext.commands import CommandNotFound
from discord.utils import get

OWNER_ID = "97153790897045504"  # Hehe, that's me!

PREFIX = "."
DESCRIPTION = "A bot made custom for Gazia's Bat Den. Just your typical chat bot! Made by Dusk-Argentum#6530."
TOKEN = os.environ.get("BBR")

bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), description=DESCRIPTION, pm_help=False, case_insensitive=True)
client = discord.Client()  # Leave this alone. I barely understand what this does, sometimes.
bot.remove_command("help")


@bot.event
async def on_ready():
    greetings_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    gamers_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    socialists_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    await greetings_role_message.add_reaction(emoji="👋")
    await gamers_role_message.add_reaction(emoji="🎮")
    await socialists_role_message.add_reaction(emoji="🗣")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("w/ batty friends! | .help"))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        error = "Command not found. View `.help` for valid commands."
    elif isinstance(error, CommandInvokeError):
        error = "Incorrect invocation. Please re-examine the command in `.help`."
    await ctx.message.channel.send(f"Error: {error}")


@bot.event
async def on_member_join(ctx):  # Welcomes a new user when they join.
    welcome_channel = bot.get_channel(290304276381564928)
    await welcome_channel.send(f"<@&636374013731667969>, {ctx.mention}! Welcome to Gazia's Bat Den! Please read <#413876271865528320>, and enjoy your stay!")


@bot.command(pass_context=True, name="test", hidden=True)  # Basically, confirm that the bot is still online.
async def test(ctx):
    """ Confirms whether or not the bot is online, basically. """
    await ctx.send("I work!")


@bot.group(pass_context=True, name="role", aliases=["r"])
async def role(ctx):
    """Adds or removes a role."""
    if ctx.invoked_subcommand is None:
        await ctx.send("Please choose a role. Valid roles: `Greetings`, `Gamers`, and `Socialists`.")


@role.command(pass_context=True, name="greetings", aliases=["gr"])
async def greetings(ctx):
    """Grants or redacts the Greetings role from you."""
    role = discord.utils.get(ctx.guild.roles, name="Greetings")
    message = ctx.message
    if role in ctx.author.roles:
        await ctx.author.remove_roles(role)
        await(await ctx.send(f"Alrighty, {ctx.author.mention}. I've removed the Greetings role from you.")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)
    else:
        await ctx.author.add_roles(role)
        await(await ctx.send(f"OK, {ctx.author.mention}! You're now a part of the Greetings role!")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)


@role.command(pass_context=True, name="gamers", aliases=["ga"])
async def gamers(ctx):
    """Grants or redacts the Gamers role from you."""
    role = discord.utils.get(ctx.guild.roles, name="Gamers")
    message = ctx.message
    if role in ctx.author.roles:
        await ctx.author.remove_roles(role)
        await(await ctx.send(f"Alrighty, {ctx.author.mention}. I've removed the Gamers role from you.")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)
    else:
        await ctx.author.add_roles(role)
        await(await ctx.send(f"OK, {ctx.author.mention}! You're now a part of the Gamers role!")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)


@role.command(pass_context=True, name="socialists", aliases=["s"])
async def socialists(ctx):
    """Grants or redacts the Socialists role from you."""
    role = discord.utils.get(ctx.guild.roles, name="Socialists")
    message = ctx.message
    if role in ctx.author.roles:
        await ctx.author.remove_roles(role)
        await(await ctx.send(f"Alrighty, {ctx.author.mention}. I've removed the Socialists role from you.")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)
    else:
        await ctx.author.add_roles(role)
        await(await ctx.send(f"OK, {ctx.author.mention}! You're now a part of the Socialists role!")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)


@bot.group(pass_context=True, name="emoji", aliases=["e", "emote"])
async def emoji(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Please enter a valid emoji. Valid emojis: [placeholder]")
    else:
        pass


@emoji.command(pass_context=True, name="pogchamp", aliases=["pog", "po"])
async def pogchamp(ctx):
    # await ctx.send(f"{ctx.author.mention} says: <:pogchamp:636572402054201368>")
    await ctx.send("<:pogchamp:636572402054201368>")


@emoji.command(pass_context=True, name="pikachu", aliases=["pika", "pi"])
async def pikachu(ctx):
    # await ctx.send(f"{ctx.author.mention} says: <:pika:636581375612289024>")
    await ctx.send("<:pika:636581375612289024>")


@bot.command(pass_context=True)
async def de(ctx, message: str):
    cmd = ctx.message
    bad = ctx.message.author
    if ctx.author.id != 97153790897045504:
        await bad.send(f"You do not have permission to use that command! Context: `.de`.")
        await cmd.delete()
    else:
        await ctx.send(message)
        await cmd.delete()


@bot.event
async def on_raw_reaction_add(event):
    greetings_emoji = "👋"
    gamers_emoji = "🎮"
    socialists_emoji = "🗣"
    greetings_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    gamers_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    socialists_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    server = bot.get_guild(event.guild_id)
    member = server.get_member(event.user_id)
    if event.message_id == 636367012372676609 and str(event.emoji) == greetings_emoji:
        role = discord.utils.get(server.roles, name="Greetings")
        if role in member.roles:
            await member.remove_roles(role)
            await member.send(f"Redacted the {str(role)} role from you.")
        else:
            await member.add_roles(role)
            await member.send(f"Here's your {str(role)} role!")
        await greetings_role_message.remove_reaction(emoji=greetings_emoji, member=member)
    elif event.message_id == 636367012372676609 and str(event.emoji) == gamers_emoji:
        role = discord.utils.get(server.roles, name="Gamers")
        if role in member.roles:
            await member.remove_roles(role)
            await member.send(f"Redacted the {str(role)} role from you.")
        else:
            await member.add_roles(role)
            await member.send(f"Here's your {str(role)} role!")
        await gamers_role_message.remove_reaction(emoji=gamers_emoji, member=member)
    elif event.message_id == 636367012372676609 and str(event.emoji) == socialists_emoji:
        role = discord.utils.get(server.roles, name="Socialists")
        if role in member.roles:
            await member.remove_roles(role)
            await member.send(f"Redacted the {str(role)} role from you.")
        else:
            await member.add_roles(role)
            await member.send(f"Here's your {str(role)} role!")
        await socialists_role_message.remove_reaction(emoji=socialists_emoji, member=member)


@bot.group(pass_context=True, name="help", aliases=["cmds", "commands", "h", "h-hewp!!!"])
async def help(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
        embed.add_field(name="General", value="`.help` \n Shows this help. \n `.test` \n Sends a test message to check if the bot's online.", inline=True)
        embed.add_field(name="Roles", value="`.role [subcommand]` `*` \n Assign yourself a specific role via command.", inline=True)
        embed.add_field(name="Emojis", value="`.emoji [subcommand]` `*` \n Have the bot print out a specific emoji.", inline=True)
        embed.add_field(name="Key Phrases", value="`fullmetal alchemist`/`Fullmetal Alchemist`/`FULLMETAL ALCHEMIST` \n Causes the bot to repeat the phrase, but louder.", inline=True)
        embed.set_footer(text="Commands denoted with a `*` have subcommands. Do `.help [command name]` for further help. Made by Dusk-Argentum#6530!")
        await ctx.send(embed=embed)
    else:
        pass


@help.command(pass_context=True)
async def role(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
    embed.add_field(name="`.role` [Subcommands]", value="`greetings` \n Adds or removes the Greetings role from you. \n `gamers` \n Adds or removes the Gamers role from you. \n `socialists` \n Adds or removes the Socialists role from you.", inline=True)
    await ctx.send(embed=embed)


@help.command(pass_context=True)
async def emoji(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
    embed.add_field(name="`.emoji` [Subcommands]", value="`pogchamp` \n Sends Pogchamp. \n `pikachu` Sends Surprised Poketch-chu.", inline=True)
    await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    if "fullmetal alchemist" in message.content and ctx.author.id != 635484274023465000:
        await ctx.send("__***FULLMETAL ALCHEMIST.***__")
    elif "Fullmetal Alchemist" in message.content and ctx.author.id != 635484274023465000:
        await ctx.send("__***FULLMETAL ALCHEMIST.***__")
    elif "FULLMETAL ALCHEMIST" in message.content and ctx.author.id != 635484274023465000:
        await ctx.send("__***FULLMETAL ALCHEMIST.***__")
    # if message.content.startswith("fullmetal alchemist") and ctx.author.id != 635484274023465000:
        # await ctx.send("__***FULLMETAL ALCHEMIST.***__")
    # elif message.content.startswith("Fullmetal Alchemist") and ctx.author.id != 635484274023465000:
        # await ctx.send("__***FULLMETAL ALCHEMIST.***__")
    # elif message.content.startswith("FULLMETAL ALCHEMIST") and ctx.author.id != 635484274023465000:
        # await ctx.send("__***FULLMETAL ALCHEMIST.***__")
    await bot.process_commands(message)


bot.run(TOKEN)
