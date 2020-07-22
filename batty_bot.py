import os


import discord
from discord.ext import commands
from discord.ext.commands import CommandInvokeError
from discord.ext.commands import CommandNotFound


import random
import re


import asyncio


import json


from datetime import datetime
import pytz


PREFIX = "."
DESCRIPTION = "A bot made custom for Gazia's Bat Den. Just your typical chat bot! Made by Dusk Argentum#6530."
TOKEN = os.environ.get("BattyBotToken")


bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), description=DESCRIPTION, pm_help=False,
                   case_insensitive=True)


bot.remove_command("help")


# Events


@bot.event
async def on_ready():
    # greetings_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    # gamers_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    # socialists_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    # turnipchamps_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    # await greetings_role_message.add_reaction(emoji="👋")
    # await gamers_role_message.add_reaction(emoji="🎮")
    # await socialists_role_message.add_reaction(emoji="🗣") ### Leave these in, in case of emergency, I guess.
    # await turnipchamps_role_message.add_reaction(emoji="<:turnipchamp:696791106653913148>")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("w/ batty friends! | .help"))
    # await bot.change_presence(status=discord.Status.online, activity=discord.CustomActivity("""Chatting with batty
    # friends! | .help""")) ## One day, this will work.


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        error = "Command not found. View `.help` for valid commands."
    elif isinstance(error, CommandInvokeError):
        error = "Incorrect invocation. Please re-examine the command in `.help`."
    elif isinstance(error, ValueError):
        error = "Incorrect invocation. Please re-examine the command in `.help`."
    await ctx.message.channel.send(f"Error: {error}")


@bot.event
async def on_member_join(ctx):  # Welcomes a new user when they join.
    if ctx.guild.id == 290304276381564928:  # Gazia's Bat Den
        welcome_channel = bot.get_channel(290304276381564928)
        await welcome_channel.send(f"""<@&636374013731667969>, {ctx.mention}!
Welcome to Gazia's Bat Den! Please read <#413876271865528320>, and enjoy your stay!""")
        return
    if ctx.guild.id == 687225286525190144:  # Snowlo
        welcome_channel = bot.get_channel(687225286525190147)
        rielle = "assets/rielle.gif"
        await welcome_channel.send(f"""Welcome, {ctx.mention}! Enjoy your stay!""")
        await welcome_channel.send(file=discord.File(rielle))
        return
    if ctx.guild.id == 348897377400258560:  # Private
        welcome_channel = bot.get_channel(348897378062827520)
        await welcome_channel.send(f"""<@97153790897045504>, {ctx.mention} has joined the server.""")
        return
    if ctx.guild.id == 657439231995543575:  # DnD
        welcome_channel = bot.get_channel(657439231995543590)
        await welcome_channel.send(f"""Welcome, {ctx.mention}, to Elysium.""")
        return
    else:
        return


@bot.event
async def on_raw_reaction_add(event):
    greetings_emoji = "👋"
    gamers_emoji = "🎮"
    socialists_emoji = "🗣"
    turnipchamps_emoji = "<:turnipchamp:696791106653913148>"
    greetings_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    gamers_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    socialists_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    turnipchamps_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    server = bot.get_guild(event.guild_id)
    member = server.get_member(event.user_id)
    if event.message_id == 636367012372676609 and str(event.emoji) == greetings_emoji:
        greetings_role = discord.utils.get(server.roles, name="Greetings")
        if greetings_role in member.roles:
            await member.remove_roles(greetings_role)
            await member.send(f"Redacted the {str(greetings_role)} role from you.")
        else:
            await member.add_roles(greetings_role)
            await member.send(f"Here's your {str(greetings_role)} role!")
        await greetings_role_message.remove_reaction(emoji=greetings_emoji, member=member)
    elif event.message_id == 636367012372676609 and str(event.emoji) == gamers_emoji:
        gamers_role = discord.utils.get(server.roles, name="Gamers")
        if gamers_role in member.roles:
            await member.remove_roles(gamers_role)
            await member.send(f"Redacted the {str(gamers_role)} role from you.")
        else:
            await member.add_roles(gamers_role)
            await member.send(f"Here's your {str(gamers_role)} role!")
        await gamers_role_message.remove_reaction(emoji=gamers_emoji, member=member)
    elif event.message_id == 636367012372676609 and str(event.emoji) == socialists_emoji:
        socialists_role = discord.utils.get(server.roles, name="Socialists")
        if socialists_role in member.roles:
            await member.remove_roles(socialists_role)
            await member.send(f"Redacted the {str(socialists_role)} role from you.")
        else:
            await member.add_roles(socialists_role)
            await member.send(f"Here's your {str(socialists_role)} role!")
        await socialists_role_message.remove_reaction(emoji=socialists_emoji, member=member)
    elif event.message_id == 636367012372676609 and str(event.emoji) == turnipchamps_emoji:
        turnipchamps_role = discord.utils.get(server.roles, name="Turnipchamps")
        if turnipchamps_role in member.roles:
            await member.remove_roles(turnipchamps_role)
            await member.send(f"Redacted the {str(turnipchamps_role)} role from you.")
        else:
            await member.add_roles(turnipchamps_role)
            await member.send(f"Here's your {str(turnipchamps_role)} role!")
        await turnipchamps_role_message.remove_reaction(emoji=turnipchamps_emoji, member=member)


# Help


@bot.group(pass_context=True, name="help_", aliases=["cmds", "commands", "h", "h-hewp!!!", "help"])
async def help_(ctx):
    """Shows a list of all commands, and whether or not a command has subcommands."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
        embed.add_field(name="Fun", value="""`.eightball`
        Gives a cryptic answer to your queries. \n `.emoji [subcommand]`
        Have the bot send a specific emoji. \n `.meme`
        Have the bot send a specific meme. \n `.rps [move]`
        Play Rock, Paper, Scissors with the bot. \n `.roll`
        Rolls dice. Format: `x`d`y`, ex. 2d6. \n `.simpleroll`
        Simply chooses a random number between 1 and your input.""", inline=False)
        embed.add_field(name="General", value="""`.help`
        Shows this help. \n `.test` 
        Sends a test message to check if the bot's online.""", inline=False)
        embed.add_field(name="Meta", value="""`.bug [name] [description]`
        Submit a bug report to the dev. \n `.suggestion [name] [description]`
        Submit a suggestion to the dev.""", inline=False)
        embed.add_field(name="Roles", value="""`.role [subcommand]` 
        Assign or redact a specific role from yourself via command.""", inline=False)
        embed.add_field(name="Key Phrases - These do not require the prefix.", value="""`Fullmetal Alchemist`
        Causes the bot to repeat the phrase, but louder. \n `/shrug`
        Sends "¯\\_(ツ)_/¯", no matter where `/shrug` is in your message. \n `2!` at the end
        Sends the "Peggle! 2!" gif meme. \n `monka`
        Sends the monkaS emoji. \n `pog`
        Sends the pogchamp emoji.""", inline=False)
        embed.set_footer(text="""If a command has subcommands, \
do `.help [command name]` for further help.\nMade by Dusk Argentum#6530!""")
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)
        return
    else:
        pass


@help_.command(pass_context=True, name="-pm")
async def pm(ctx):
    """PMs the help message to the invoker."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
    embed.add_field(name="Fun", value="""`.eightball`
            Gives a cryptic answer to your queries. \n `.emoji [subcommand]`
            Have the bot send a specific emoji. \n `.meme`
            Have the bot send a specific meme. \n `.rps [move]`
            Play Rock, Paper, Scissors with the bot. \n `.roll`
            Rolls dice. Format: `x`d`y`, ex. 2d6. \n `.simpleroll`
            Simply chooses a random number between 1 and your input.""", inline=False)
    embed.add_field(name="General", value="""`.help`
            Shows this help. \n `.test` 
            Sends a test message to check if the bot's online.""", inline=False)
    embed.add_field(name="Meta", value="""`.bug [name] [description]`
            Submit a bug report to the dev. \n `.suggestion [name] [description]`
            Submit a suggestion to the dev.""", inline=False)
    embed.add_field(name="Roles", value="""`.role [subcommand]` 
            Assign or redact a specific role from yourself via command.""", inline=False)
    embed.add_field(name="Key Phrases - These do not require the prefix.", value="""`Fullmetal Alchemist`
            Causes the bot to repeat the phrase, but louder. \n `/shrug`
            Sends "¯\\_(ツ)_/¯", no matter where `/shrug` is in your message. \n `2!` at the end
            Sends the "Peggle! 2!" gif meme. \n `monka`
            Sends the monkaS emoji. \n `pog`
            Sends the pogchamp emoji.""", inline=False)
    embed.set_footer(text="""If a command has subcommands, \
    do `.help [command name]` for further help.\nMade by Dusk Argentum#6530!""")
    embed.set_thumbnail(url=url)
    await ctx.author.send(embed=embed)
    return


@help_.group(pass_context=True, name="help__", aliases=["cmds", "commands", "h", "h-hewp!!!", "help"])
async def help__(ctx):
    """The help entry for `.help`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="`.help`", color=discord.Color(0xE9B52A), description="""Aliases: 
    `.cmds`, `.commands`, `.h`, `.h-hewp!!!`.""")
        embed.add_field(name="Function:", value="Shows the help for Batty Bot.", inline=False)
        embed.add_field(name="Possible Arguments:", value="""`-pm` \n PMs the help to you, \
instead of posting it in the invoking channel.""", inline=False)
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)
        return
    else:
        pass


@help__.command(pass_context=True, name="-pm")
async def pm(ctx):
    """The PM'd help entry for `.help`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    embed = discord.Embed(title="`.help`", color=discord.Color(0xE9B52A), description="""Aliases: 
        `.cmds`, `.commands`, `.h`, `.h-hewp!!!`.""")
    embed.add_field(name="Function:", value="Shows the help for Batty Bot.", inline=False)
    embed.add_field(name="Possible Arguments:", value="""`-pm` \n PMs the help to you, \
instead of posting it in the invoking channel.""", inline=False)
    embed.set_thumbnail(url=url)
    await ctx.author.send(embed=embed)
    return


@help_.group(pass_context=True)
async def test(ctx):
    """The help entry for `.test`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="`.test`", color=discord.Color(0xE9B52A))
        embed.add_field(name="Function:", value="Sends a test message to check if the bot's online.", inline=False)
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)
        return
    else:
        pass


@test.command(pass_context=True, name="-pm")
async def pm(ctx):
    """The PM'd help entry for `.test`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    embed = discord.Embed(title="`.test`", color=discord.Color(0xE9B52A))
    embed.add_field(name="Function:", value="Sends a test message to check if the bot's online.", inline=False)
    embed.set_thumbnail(url=url)
    await ctx.author.send(embed=embed)
    return


@help_.group(pass_context=True)
async def role(ctx):
    """The help entry for `.role`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="`.role`", color=discord.Color(0xE8B52A))
        embed.add_field(name="Function:", value="""Assign or redact a specific role from yourself via command.""",
                        inline=False)
        embed.add_field(name="Possible Arguments:", value="""`gamers` \n  Assigns or redacts the Gamers role from you.
        `greetings` \n Assigns or redacts the Greetings role from you. \n `socialists` \n Assigns or redacts the
        Socialists role from you. \n `turnipchamps` \n Assigns or redacts the Turnipchamps role from you.""",
                        inline=False)
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)
        return
    else:
        pass


@role.command(pass_context=True, name="-pm")
async def pm(ctx):
    """THe PM'd help entry for `.role`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    embed = discord.Embed(title="`.role`", color=discord.Color(0xE8B52A))
    embed.add_field(name="Function:", value="""Assign or redact a specific role from yourself via command.""",
                    inline=False)
    embed.add_field(name="Possible Arguments:", value="""`gamers` \n  Assigns or redacts the Gamers role from you.
    `greetings` \n Assigns or redacts the Greetings role from you. \n `socialists` \n Assigns or redacts the
    Socialists role from you. \n `turnipchamps` \n Assigns or redacts the Turnipchamps role from you.""",
                    inline=False)
    embed.set_thumbnail(url=url)
    await ctx.author.send(embed=embed)
    return


@help_.group(pass_context=True, aliases=["8", "8ball"])
async def eightball(ctx):
    """The help entry for `.eightball`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="`.eightball`", color=discord.Color(0xE8B52A), description="""Aliases:
        `.8`, `.8ball`.""")
        embed.add_field(name="Function:", value="Gives a cryptic answer to your queries.", inline=False)
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)
        return
    else:
        pass


@eightball.command(pass_context=True, name="-pm")
async def pm(ctx):
    """The PM'd help entry for `.eightball`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    embed = discord.Embed(title="`.eightball`", color=discord.Color(0xE8B52A), description="""Aliases:
            `.8`, `.8ball`.""")
    embed.add_field(name="Function:`", value="Gives a cryptic answer to your queries.", inline=False)
    embed.set_thumbnail(url=url)
    await ctx.author.send(embed=embed)
    return


@help_.group(pass_context=True, aliases=["e"])
async def emoji(ctx):
    """The help entry for `.emoji`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    if ctx.invoked_subcommand is None:
        """Help for `.emoji`."""
        embed = discord.Embed(title="`.emoji`", color=discord.Color(0xE8B52A), description="""Aliases:
        `.e`.""")
        embed.add_field(name="Function:", value="""Have the bot print out a specific emoji.""", inline=False)
        embed.add_field(name="Accepted Arguments:", value="""`monkas` \n Sends monkaS. \n `pikachu`
        Sends Surprised Pikachu, in the style of the Poketch. \n `pogchamp` \n Sends Pogchamp.""", inline=False)
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)
        return
    else:
        pass


@emoji.command(pass_context=True, name="-pm")
async def pm(ctx):
    """The PM'd help entry for `.emoji`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    embed = discord.Embed(title="`.emoji`", color=discord.Color(0xE8B52A), description="""Aliases:
    `.e`.""")
    embed.add_field(name="Function:", value="""Have the bot print out a specific emoji.""", inline=False)
    embed.add_field(name="Accepted Arguments:", value="""`monkas` \n Sends monkaS. \n `pikachu`
    Sends Surprised Pikachu, in the style of the Poketch. \n `pogchamp` \n Sends Pogchamp.""", inline=False)
    embed.set_thumbnail(url=url)
    await ctx.author.send(embed=embed)
    return


@help_.group(pass_context=True, aliases=["m"])
async def meme(ctx):
    """The help entry for `.meme`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="`.meme`", color=discord.Color(0xE8B52A), description="""Aliases:
        `.m`.""")
        embed.add_field(name="Function:", value="Send a specific meme.", inline=False)
        embed.add_field(name="Accepted Arguments:", value="""`chime` \n Sends the "Oh? You're a chime?" meme. \n `typo`
         \n Sends the "TYPO! In the Groupchat" meme. \n
        `wig` \n Sends the "Wig" meme. \n `wig2` \n Sends a "Wig" video clip.""", inline=False)
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)
        return
    else:
        pass


@meme.group(pass_context=True, name="-pm")
async def pm(ctx):
    """The PM'd help entry for `.meme`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    embed = discord.Embed(title="`.meme`", color=discord.Color(0xE8B52A), description="""Aliases:
    `.m`.""")
    embed.add_field(name="Function:", value="Send a specific meme.", inline=False)
    embed.add_field(name="Accepted Arguments:", value="""`chime` \n Sends the "Oh? You're a chime?" meme. \n `typo`
     \n Sends the "TYPO! In the Groupchat" meme. \n
    `wig` \n Sends the "Wig" meme. \n `wig2` \n Sends a "Wig" video clip.""", inline=False)
    embed.set_thumbnail(url=url)
    await ctx.author.send(embed=embed)
    return


@help_.group(pass_context=True, aliases=["rockpaperscissors"])
async def rps(ctx):
    """The help entry for `.rps`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="`.rps`", color=discord.Color(0xE8B52A), description="""Aliases:
        `.rockpaperscissors`.""")
        embed.add_field(name="Function:", value="Play Rock, Paper, Scissors with the bot.", inline=False)
        embed.add_field(name="Accepted Arguments:", value="""`rock` \n Play as Rock. \n `paper`
        Play as Paper. \n `scissors` \n Play as scissors.""", inline=False)
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)
        return
    else:
        pass


@rps.group(pass_context=True, name="-pm")
async def pm(ctx):
    """The PM'd help entry for `.rps`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    embed = discord.Embed(title="`.rps`", color=discord.Color(0xE8B52A), description="""Aliases:
    `.rockpaperscissors`.""")
    embed.add_field(name="Function:", value="Play Rock, Paper, Scissors with the bot.", inline=False)
    embed.add_field(name="Accepted Arguments:", value="""`rock` \n Play as Rock. \n `paper`
    Play as Paper. \n `scissors` \n Play as scissors.""", inline=False)
    embed.set_thumbnail(url=url)
    await ctx.author.send(embed=embed)
    return


@help_.group(pass_context=True, aliases=["r"])
async def roll(ctx):
    """The help entry for `.roll`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="`.roll`", color=discord.Color(0xE8B52A), description="""Aliases:
        `.r`.""")
        embed.add_field(name="Function:", value="Rolls dice. Format: `x`d`y`, ex. 2d6.", inline=False)
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)
        return
    else:
        pass


@roll.group(pass_context=True, name="-pm")
async def pm(ctx):
    """The PM'd help entry for `.roll`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    embed = discord.Embed(title="`.roll`", color=discord.Color(0xE8B52A), description="""Aliases:
    `.r`.""")
    embed.add_field(name="Function:", value="Rolls dice. Format: `x`d`y`, ex. 2d6.", inline=False)
    embed.set_thumbnail(url=url)
    await ctx.author.send(embed=embed)
    return


@help_.group(pass_context=True, aliases=["sr", "simp"])
async def simpleroll(ctx):
    """The help entry for `.simpleroll`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="`.simpleroll`", color=discord.Color(0xE8B52A), description="""Aliases:
        `.sr`, `simp`.""")
        embed.add_field(name="Function:", value="""Simply chooses a random number between 1 and your input.""",
                        inline=False)
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)
        return
    else:
        pass


@simpleroll.command(pass_context=True, name="-pm")
async def pm(ctx):
    """The PM'd help entry for `.simpleroll`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    embed = discord.Embed(title="`.simpleroll`", color=discord.Color(0xE8B52A), description="""Aliases:
            `.sr`, `simp`.""")
    embed.add_field(name="`Function:", value="""Simply chooses a random number between 1 and your input.""",
                    inline=False)
    embed.set_thumbnail(url=url)
    await ctx.author.send(embed=embed)
    return


@help_.group(pass_context=True, name="bug")
async def bug(ctx):
    """The help entry for `.bug`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="`.bug`", color=discord.Color(0xE8B52A))
        embed.add_field(name="Function:", value="Submit a bug report to the dev.", inline=False)
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)
        return
    else:
        pass


@bug.command(pass_context=True, name="-pm")
async def pm(ctx):
    """The PM'd help entry for `.bug`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    embed = discord.Embed(title="`.bug`", color=discord.Color(0xE8B52A))
    embed.add_field(name="Function:", value="Submit a bug report to the dev.", inline=False)
    embed.set_thumbnail(url=url)
    await ctx.author.send(embed=embed)
    return


@help_.group(pass_context=True, name="suggestion", aliases=["s", "suggest"])
async def suggestion(ctx):
    """The help entry for `.suggestion`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="`.suggestion`", color=discord.Color(0xE8B52A), description="""Aliases:
        `.s`, `.suggest`.""")
        embed.add_field(name="Function:", value="Submit a suggestion to the dev.", inline=False)
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)
        return
    else:
        pass


@suggestion.command(pass_context=True, name="-pm")
async def pm(ctx):
    """The PM'd help entry for `.suggestion`."""
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    embed = discord.Embed(title="`.suggestion`", color=discord.Color(0xE8B52A), description="""Aliases:
    `.s`, `.suggest`.""")
    embed.add_field(name="Function:", value="Submit a suggestion to the dev.", inline=False)
    embed.set_thumbnail(url=url)
    await ctx.author.send(embed=embed)
    return


# DnD-SERVER EXCLUSIVE COMMANDS


@bot.group(pass_context=True, name="color", aliases=["c"])
async def color(ctx, color=None):
    """Changes your role's color. Only usable on Dusk's DnD server."""
    cmd = ctx.message
    cmduser = ctx.message.author
    server = bot.get_guild(ctx.guild.id)
    player1role = discord.utils.get(server.roles, id=722553852011741214)
    player2role = discord.utils.get(server.roles, id=722553954596159622)
    player3role = discord.utils.get(server.roles, id=722553971813646366)
    player4role = discord.utils.get(server.roles, id=722553985118240789)
    player5role = discord.utils.get(server.roles, id=722554001165385829)
    if server.id != 657439231995543575:
        await cmduser.send(f"This command is not available on the server you're trying to use it on!")
        await cmd.delete()
        return
    elif server.id == 657439231995543575:
        color_input = re.search(r"([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])([0-9]|[a-f])",
                                str(color), re.IGNORECASE)
        color_input_random = re.search(r"random", str(color), re.IGNORECASE)
        if color_input_random:
            random_color = random.randint(1, 16777215)
            if player1role in cmduser.roles:
                await player1role.edit(color=discord.Color(int(random_color)))
                await ctx.send(f"I have changed {player1role.mention}'s color.")
                return
            if player2role in cmduser.roles:
                await player2role.edit(color=discord.Color(int(random_color)))
                await ctx.send(f"I have changed {player2role.mention}'s color.")
                return
            if player3role in cmduser.roles:
                await player3role.edit(color=discord.Color(int(random_color)))
                await ctx.send(f"I have changed {player3role.mention}'s color.")
                return
            if player4role in cmduser.roles:
                await player4role.edit(color=discord.Color(int(random_color)))
                await ctx.send(f"I have changed {player4role.mention}'s color.")
                return
            if player5role in cmduser.roles:
                await player5role.edit(color=discord.Color(int(random_color)))
                await ctx.send(f"I have changed {player5role.mention}'s color.")
                return
        if color_input is None:
            await ctx.send("""That's not a valid color! Please make sure it is a hex code **without** the \
`#` at the beginning.""")
            return
        else:
            if player1role in cmduser.roles:
                await player1role.edit(color=discord.Color(int(color, 16)))
                await ctx.send(f"I have changed {player1role.mention}'s color to #{color}.")
                return
            if player2role in cmduser.roles:
                await player2role.edit(color=discord.Color(int(color, 16)))
                await ctx.send(f"I have changed {player2role.mention}'s color to #{color}.")
                return
            if player3role in cmduser.roles:
                await player3role.edit(color=discord.Color(int(color, 16)))
                await ctx.send(f"I have changed {player3role.mention}'s color to #{color}.")
                return
            if player4role in cmduser.roles:
                await player4role.edit(color=discord.Color(int(color, 16)))
                await ctx.send(f"I have changed {player4role.mention}'s color to #{color}.")
                return
            if player5role in cmduser.roles:
                await player5role.edit(color=discord.Color(int(color, 16)))
                await ctx.send(f"I have changed {player5role.mention}'s color to #{color}.")
                return
            else:
                await cmduser.send("You should also not see this.")
                return
    else:
        await cmduser.send("You should not see this message.")
        return


@bot.group(pass_context=True, name="name", aliases=["n"])
async def name(ctx, *, name: str = None):
    """Changes your role's color. Only usable on Dusk's DnD server."""
    cmd = ctx.message
    cmduser = ctx.message.author
    server = bot.get_guild(ctx.guild.id)
    player1role = discord.utils.get(server.roles, id=722553852011741214)
    player2role = discord.utils.get(server.roles, id=722553954596159622)
    player3role = discord.utils.get(server.roles, id=722553971813646366)
    player4role = discord.utils.get(server.roles, id=722553985118240789)
    player5role = discord.utils.get(server.roles, id=722554001165385829)
    if server.id != 657439231995543575:
        await cmduser.send(f"This command is not available on the server you're trying to use it on!")
        await cmd.delete()
        return
    elif server.id == 657439231995543575:
        name_input = re.search(r".{1,99}", name, re.IGNORECASE)
        if name_input is None:
            await ctx.send("""That's not a valid name! Please make sure it has less than 100 characters.""")
            return
        if name is None:
            await ctx.send("""That's not a valid name!""")
            return
        else:
            if player1role in cmduser.roles:
                await player1role.edit(name=str(name))
                await ctx.send(f"I have changed {player1role.mention}'s name.")
                return
            if player2role in cmduser.roles:
                await player2role.edit(name=str(name))
                await ctx.send(f"I have changed {player2role.mention}'s name.")
                return
            if player3role in cmduser.roles:
                await player3role.edit(name=str(name))
                await ctx.send(f"I have changed {player3role.mention}'s name.")
                return
            if player4role in cmduser.roles:
                await player4role.edit(name=str(name))
                await ctx.send(f"I have changed {player4role.mention}'s name.")
                return
            if player5role in cmduser.roles:
                await player5role.edit(name=str(name))
                await ctx.send(f"I have changed {player5role.mention}'s name.")
                return
            else:
                await cmduser.send("You should also not see this.")
                return
    else:
        await cmduser.send("You should not see this message.")
        return


# FUN


@bot.command(pass_context=True, name="eightball", aliases=["8", "8ball"])
async def eightball(ctx):
    """Gives a cryptic answer to your queries."""
    answer = random.choice(["Yes.", "No.", "Possibly.", "Not likely.", "It's up to you.", "It's out of your control.",
                            "I can't say.", "That is beyond the scope of my programming."])
    await ctx.send(answer)
    return


@bot.group(pass_context=True, name="emoji", aliases=["e", "emote"])
async def emoji(ctx):
    """Prints a specific emoji."""
    if ctx.invoked_subcommand is None:
        await ctx.send("Please enter a valid emoji. Valid emojis: `monkas`, `pogchamp`, `pikachu`.")
        return
    else:
        return


@emoji.command(pass_context=True, name="pogchamp", aliases=["pog", "po"])
async def pogchamp(ctx):
    # await ctx.send(f"{ctx.author.mention} says: <:pogchamp:636572402054201368>") ### Do not delete this.
    await ctx.send("<:pogchamp:636572402054201368>")
    return


@emoji.command(pass_context=True, name="pikachu", aliases=["pika", "pi"])
async def pikachu(ctx):
    # await ctx.send(f"{ctx.author.mention} says: <:pika:636581375612289024>") ### Do not delete this.
    await ctx.send("<:pika:636581375612289024>")
    return


@emoji.command(pass_context=True, name="monkas", aliases=["m", "monkaS", "monka"])
async def monkas(ctx):
    # await ctx.send(f"{ctx.author.mention} says: <:monkas:645002369091764284>") ### Do not delete this.
    await ctx.send("<:monkas:636575202217689099>")
    return


@bot.group(pass_context=True, name="meme", aliases=["m"])
async def meme(ctx):
    """Prints a specific meme."""
    if ctx.invoked_subcommand is None:
        await ctx.send("Please enter a valid meme. Valid memes: `chime`, `typo`, `wig`, `wig2`.")
        return
    else:
        return


@meme.command(pass_context=True, name="chime", aliases=["c"])
async def chime(ctx):
    """Sends the "Oh? You're a chime?" meme."""
    image = "assets/chime.jpeg"
    await ctx.send(file=discord.File(image))
    return


@meme.command(pass_context=True, name="typo", aliases=["t"])
async def typo(ctx):
    """Sends the "TYPO! In the Groupchat" meme."""
    image = "assets/typo.jpg"
    await ctx.send(file=discord.File(image))
    return


@meme.command(pass_context=True, name="wig", aliases=["w"])
async def wig(ctx):
    """Sends the "Wig" meme."""
    image = "assets/wig.jpg"
    await ctx.send(file=discord.File(image))
    return


@meme.command(pass_context=True, name="wig2", aliases=["w2"])
async def wig2(ctx):
    """Y'all ready?"""
    video = "assets/wig.mp4"
    await ctx.send(file=discord.File(video))
    return


@bot.command(pass_context=True, name="rps", aliases=["rockpaperscissors"])
async def rps(ctx, move):
    """Play Rock, Paper, Scissors with the bot."""
    title = "RPS: Results!"
    win_color = discord.Color(0x02e64a)
    lose_color = discord.Color(0x99122b)
    draw_color = discord.Color(0x52575e)
    win_desc = f"You win, {ctx.author.mention}!"
    lose_desc = f"I win, {ctx.author.mention}."
    draw_desc = f"We drew, {ctx.author.mention}."
    player_move = move.lower()
    bot_move = random.choice(["rock", "paper", "scissors"])
    if player_move not in "rock paper scissors":
        await ctx.send("Invalid move! Valid moves: Rock, Paper, Scissors.")
    else:
        if player_move == "rock" and bot_move == "rock":
            embed = discord.Embed(title=title, color=draw_color, description=f"I got Rock... {draw_desc}")
            await ctx.send(embed=embed)
            return
        elif player_move == "rock" and bot_move == "paper":
            embed = discord.Embed(title=title, color=lose_color, description=f"I got Paper... {lose_desc}")
            await ctx.send(embed=embed)
            return
        elif player_move == "rock" and bot_move == "scissors":
            embed = discord.Embed(title=title, color=win_color, description=f"I got Scissors... {win_desc}")
            await ctx.send(embed=embed)
            return
        elif player_move == "paper" and bot_move == "rock":
            embed = discord.Embed(title=title, color=win_color, description=f"I got Rock... {win_desc}")
            await ctx.send(embed=embed)
            return
        elif player_move == "paper" and bot_move == "paper":
            embed = discord.Embed(title=title, color=draw_color, description=f"I got Paper... {draw_desc}")
            await ctx.send(embed=embed)
            return
        elif player_move == "paper" and bot_move == "scissors":
            embed = discord.Embed(title=title, color=lose_color, description=f"I got Scissors... {lose_desc}")
            await ctx.send(embed=embed)
            return
        elif player_move == "scissors" and bot_move == "rock":
            embed = discord.Embed(title=title, color=lose_color, description=f"I got Rock... {lose_desc}")
            await ctx.send(embed=embed)
            return
        elif player_move == "scissors" and bot_move == "paper":
            embed = discord.Embed(title=title, color=win_color, description=f"I got Paper... {win_desc}")
            await ctx.send(embed=embed)
            return
        elif player_move == "scissors" and bot_move == "scissors":
            embed = discord.Embed(title=title, color=draw_color, description=f"I got Scissors... {draw_desc}")
            await ctx.send(embed=embed)
            return


@bot.command(pass_context=True, name="roll", aliases=["r"])
async def roll(ctx, *args):
    """Rolls dice. Format: `x`d`y`, ex. 2d6."""
    a = " ".join(args)
    p = " + "
    setup = re.fullmatch(r"(?P<howmany>[0-9]+)d(?P<howmuch>[0-9]+)", a, re.IGNORECASE)
    result = []
    resultstr = []
    hma = int(setup.group("howmany"))
    hmu = int(setup.group("howmuch"))
    url = "https://cdn.discordapp.com/attachments/627784999873019914/718981774440661022/battypride.png"
    if setup:
        if hma >= 100:
            await ctx.send("Do you... really need to roll so many dice..?")
            return
        elif hmu >= 100:
            await ctx.send("Do you... really need to roll dice with so many sides..?")
            return
        elif hma == 0:
            await ctx.send("Please provide one or more dice to roll.")
            return
        elif hmu == 0:
            await ctx.send("Please provide the amount of sides you wish your dice to have.")
            return
        else:
            pass
        if 100 >= hma > 1:
            for x in range(hma):
                value = random.randint(1, hmu)
                result.append(int(value))
                resultstr.append(str(value))
            total = sum(result)
            embed = discord.Embed(title=f"Rolling {hma}d{hmu}...", color=discord.Color(0xE8B52A))
            embed.add_field(name="Result:", value=f"{p.join(resultstr)} = **{str(total)}**")
            embed.set_thumbnail(url=url)
            await ctx.send(embed=embed)
            return
        elif hma == 1:
            for x in range(hma):
                value = random.randint(1, hmu)
                result.append(int(value))
                resultstr.append(str(value))
            embed = discord.Embed(title=f"Rolling {hma}d{hmu}...", color=discord.Color(0xE8B52A))
            embed.set_thumbnail(url=url)
            embed.add_field(name="Result:", value=f"{a.join(resultstr)}")
            await ctx.send(embed=embed)
            return
    else:
        await ctx.send("Please use a valid dice format. Example: `2d10`.")
        return


@bot.command(pass_context=True, name="simpleroll", aliases=["sr", "simp"])
async def simpleroll(ctx, *, howmuch: int):
    """Simply chooses a random number between 1 and your input."""
    if howmuch >= 1000:
        await ctx.send(f"Do you... really need to generate such a high number..?")
        return
    else:
        for x in range(1):
            result = random.randint(1, howmuch)
            await ctx.send(f"{ctx.author.mention}: {result}.")
            return


# GENERAL


@bot.command(pass_context=True, name="test")  # Basically, confirm that the bot is still online.
async def test(ctx):
    """Confirms whether or not the bot is online, basically."""
    await ctx.send("I work!")
    return


# META


@bot.command(pass_context=True, name="bug")
async def bug(ctx, bugname, *args):
    """Submits a bug to the dev."""
    avatar = ctx.message.author.avatar_url
    channel = bot.get_channel(645409157217910794)
    await ctx.send(f"Thanks for your bug report, {ctx.author}! Does this bug report look right?")
    embed = discord.Embed(title=f"Bug Report: {bugname}", color=discord.Color(0xa8411e))
    embed.add_field(name=f"{ctx.author} reports:", value=" ".join(args))
    embed.set_thumbnail(url=avatar)
    embed.set_footer(text=f"""If this looks right, give it a thumbs up! If not, redo the bug report.
If the bug report name got cut off, redo the bug report with quotes surrounding the name!""")
    await ctx.send(embed=embed)

    def check(reaction, user):
        return user == ctx.message.author and str(reaction.emoji) == "👍"

    try:
        reaction, user = await bot.wait_for("reaction_add", timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("Bug report not sent. Awaited 👍, got nothing.")
        return
    else:
        await ctx.send("OK! I've sent off your bug report.")
        embed2 = discord.Embed(title=f"Bug Report: {bugname}", color=discord.Color(0xa8411e))
        embed2.add_field(name=f"{ctx.author} reports:", value=" ".join(args))
        embed2.set_thumbnail(url=avatar)
        await channel.send(embed=embed2)
        return


@bot.command(pass_context=True, name="github", aliases=["git", "g"])
async def github(ctx):
    """Prints a link to Batty Bot's github page."""
    await ctx.send(f"""Fancy yourself a coder? Feel like submitting your very own feature for Batty Bot?
Contribute to the Github here! https://github.com/Dusk-Argentum/batty_bot""")
    return


@bot.command(pass_context=True, name="suggestion", aliases=["suggest", "s"])
async def suggestion(ctx, suggestionname, *args):
    """Submits a suggestion to the dev."""
    avatar = ctx.message.author.avatar_url
    channel = bot.get_channel(645409183348424706)
    await ctx.send(f"Thanks for your suggestion, {ctx.author}! Does this suggestion look right?")
    embed = discord.Embed(title=f"Suggestion: {suggestionname}", color=discord.Color(0x057a51))
    embed.add_field(name=f"{ctx.author} says:", value=" ".join(args))
    embed.set_thumbnail(url=avatar)
    embed.set_footer(text=f"""If this looks right, give it a thumbs up! If not, redo the suggestion.
If the suggestion name got cut off, redo the suggestion with quotes surrounding the name!""")
    await ctx.send(embed=embed)

    def check(reaction, user):
        return user == ctx.message.author and str(reaction.emoji) == "👍"

    try:
        reaction, user = await bot.wait_for("reaction_add", timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("Suggestion not sent. Awaited 👍, got nothing.")
        return
    else:
        await ctx.send("OK! I've sent off your suggestion.")
        embed2 = discord.Embed(title=f"Suggestion: {suggestionname}", color=discord.Color(0x057a51))
        embed2.add_field(name=f"{ctx.author} requests:", value=" ".join(args))
        embed2.set_thumbnail(url=avatar)
        await channel.send(embed=embed2)
        return

# ROLE


@bot.group(pass_context=True, name="role")
async def role(ctx):
    """Adds or removes a role."""
    if ctx.invoked_subcommand is None:
        await ctx.send("Please choose a role. Valid roles: `Gamers`, `Greetings`, `Socialists`, and `Turnipchamps`.")
        return


@role.command(pass_context=True, name="greetings", aliases=["gr"])
async def greetings(ctx):
    """Adds or removes the Greetings role from you."""
    greetings_role = discord.utils.get(ctx.guild.roles, name="Greetings")
    message = ctx.message
    if greetings_role in ctx.author.roles:
        await ctx.author.remove_roles(greetings_role)
        await(await ctx.send(f"Alrighty, {ctx.author.mention}. I've removed the Greetings role from you.")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)
        return
    else:
        await ctx.author.add_roles(greetings_role)
        await(await ctx.send(f"OK, {ctx.author.mention}! You're now a part of the Greetings role!")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)
        return


@role.command(pass_context=True, name="gamers", aliases=["ga"])
async def gamers(ctx):
    """Adds or removes the Gamers role from you."""
    gamers_role = discord.utils.get(ctx.guild.roles, name="Gamers")
    message = ctx.message
    if gamers_role in ctx.author.roles:
        await ctx.author.remove_roles(gamers_role)
        await(await ctx.send(f"Alrighty, {ctx.author.mention}. I've removed the Gamers role from you.")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)
        return
    else:
        await ctx.author.add_roles(gamers_role)
        await(await ctx.send(f"OK, {ctx.author.mention}! You're now a part of the Gamers role!")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)
        return


@role.command(pass_context=True, name="socialists", aliases=["s"])
async def socialists(ctx):
    """Adds or removes the Socialists role from you."""
    socialists_role = discord.utils.get(ctx.guild.roles, name="Socialists")
    message = ctx.message
    if socialists_role in ctx.author.roles:
        await ctx.author.remove_roles(socialists_role)
        await(await ctx.send(f"Alrighty, {ctx.author.mention}. I've removed the Socialists role from you.")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)
        return
    else:
        await ctx.author.add_roles(socialists_role)
        await(await ctx.send(f"OK, {ctx.author.mention}! You're now a part of the Socialists role!")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)
        return


@role.command(pass_context=True, name="turnipchamps", aliases=["t"])
async def turnipchamps(ctx):
    """Adds or removes the Turnipchamps role from you."""
    turnipchamps_role = discord.utils.get(ctx.guild.roles, name="Turnipchamps")
    message = ctx.message
    if turnipchamps_role in ctx.author.roles:
        await ctx.author.remove_roles(turnipchamps_role)
        await(await ctx.send(f"Alrighty, {ctx.author.mention}. I've removed the Turnipchamps role from you.")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)
        return
    else:
        await ctx.author.add_roles(turnipchamps_role)
        await(await ctx.send(f"OK, {ctx.author.mention}! You're now a part of the Turnipchamps role!")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)
        return


# MODERATION (INTERNAL)


@bot.command(pass_context=True, name="ban", aliases=["b"])
async def ban(ctx, member: discord.Member = None, *, reason: str = "Unspecified reason."):
    """Bans a user from a server via @mention."""
    cmd = ctx.message
    cmduser = ctx.message.author
    server = bot.get_guild(ctx.guild.id)
    user = server.get_member(ctx.author.id)
    moderator_role = discord.utils.get(server.roles, name="Moderator")
    mod_log_channel = discord.utils.get(server.channels, name="mod_log")
    url = member.avatar_url
    if moderator_role in user.roles:
        if member is None:
            await cmduser.send(f"Invalid member. To select a member, @mention them.")
            return
        elif moderator_role in member.roles:
            await cmduser.send(f"You cannot punish that user! They are a Moderator.")
            return
        else:
            await cmd.guild.ban(member, reason=reason, delete_message_days=1)
            await cmd.add_reaction("👍")
            if mod_log_channel is None:
                await cmduser.send(f"""Action successfully completed. To enable moderation command logging, \
please create a channel named `#mod_log`.""")
                return
            else:
                embed = discord.Embed(title=f"Banhammer swung.", color=discord.Color(0xa81707))
                embed.add_field(name=f"Responsible Mod:", value=f"{cmduser.mention} ({cmduser.id})", inline=True)
                embed.add_field(name=f"Action Taken On:", value=f"{member.mention} ({member.id})", inline=True)
                embed.add_field(name=f"Reason:", value=f"{reason}", inline=False)
                embed.set_thumbnail(url=url)
                await mod_log_channel.send(embed=embed)
                await cmd.add_reaction("📜")
                return
    elif ctx.author.id == 157298325014577152:
        tear_that_bitch_apart_channel = discord.utils.get(ctx.guild.channels, id=687225286525190147)
        if member is None:
            await cmduser.send(f"Invalid member. To select a member, @mention them.")
            return
        elif moderator_role in member.roles:
            await cmduser.send(f"You cannot punish that user! They are a Moderator.")
            return
        else:
            await cmd.guild.ban(member, reason=reason, delete_message_days=1)
            await cmd.add_reaction("👍")
            if mod_log_channel is None:
                await cmduser.send(f"""Action successfully completed. To enable moderation command logging, \
please create a channel named `#mod_log`.""")
                return
            else:
                embed = discord.Embed(title=f"Banhammer swung.", color=discord.Color(0xa81707))
                embed.add_field(name=f"Responsible Mod:", value=f"{cmduser.mention} ({cmduser.id})", inline=True)
                embed.add_field(name=f"Action Taken On:", value=f"{member.mention} ({member.id})", inline=True)
                embed.add_field(name=f"Reason:", value=f"{reason}", inline=False)
                embed.set_thumbnail(url=url)
                embed.set_footer(text="Maybe you shouldn't've been cringe.")
                await tear_that_bitch_apart_channel.send(embed=embed)
                await cmd.add_reaction("📜")
                return
    else:
        await cmduser.send(f"""You do not have permission to run that command! Context: `.ban`. \
You must have the role `Moderator` to run this command.""")
        await cmd.delete()
        return


@bot.command(pass_context=True, name="forceban", aliases=["fb"])
async def forceban(ctx, member_id: int = None, *, reason: str = "Unspecified reason."):
    """Forcefully bans a user via ID."""
    cmd = ctx.message
    cmduser = ctx.message.author
    server = bot.get_guild(ctx.guild.id)
    user = server.get_member(ctx.author.id)
    moderator_role = discord.utils.get(server.roles, name="Moderator")
    mod_log_channel = discord.utils.get(server.channels, name="mod_log")
    url = ctx.author.avatar_url
    if moderator_role in user.roles:
        if member_id is None:
            await cmduser.send(f"Invalid member. To select a member, use their ID.")
            return
        elif moderator_role in member.roles:
            await cmduser.send(f"You cannot punish that user! They are a Moderator.")
            return
        else:
            await cmd.guild.ban(discord.Object(id=member_id), reason=reason, delete_message_days=1)
            await cmd.add_reaction("👍")
            if mod_log_channel is None:
                await cmduser.send(f"""Action successfully completed. To enable moderation command logging, \
please create a channel named `#mod_log`.""")
                return
            else:
                embed = discord.Embed(title=f"Banhammer swung with force.", color=discord.Color(0x95a5a6))
                embed.add_field(name=f"Responsible Mod:", value=f"{cmduser.mention} ({cmduser.id})", inline=True)
                embed.add_field(name=f"Action Taken On:", value=f"{member_id}", inline=True)
                embed.add_field(name=f"Reason:", value=f"{reason}", inline=False)
                embed.set_thumbnail(url=url)
                await mod_log_channel.send(embed=embed)
                await cmd.add_reaction("📜")
                return
    else:
        await cmduser.send(f"""You do not have permission to run that command! Context: `.ban`. \
You must have the role `Moderator` to run this command.""")
        return


@bot.command(pass_context=True, name="kick", aliases=["k"])
async def kick(ctx, member: discord.Member = None, *, reason: str = "Unspecified reason."):
    """Kicks a user from a server via @mention."""
    cmd = ctx.message
    cmduser = ctx.message.author
    server = bot.get_guild(ctx.guild.id)
    user = server.get_member(ctx.author.id)
    moderator_role = discord.utils.get(server.roles, name="Moderator")
    mod_log_channel = discord.utils.get(server.channels, name="mod_log")
    url = member.avatar_url
    if moderator_role in user.roles:
        if member is None:
            await cmduser.send(f"Invalid member. To select a member, @mention them.")
            return
        elif moderator_role in member.roles:
            await cmduser.send(f"You cannot punish that user! They are a Moderator.")
            return
        else:
            await cmd.guild.kick(member, reason=reason)
            await cmd.add_reaction("👍")
            if mod_log_channel is None:
                await cmduser.send(f"""Action successfully completed. To enable moderation command logging, \
please create a channel named `#mod_log`.""")
                return
            else:
                embed = discord.Embed(title=f"Kick performed.", color=discord.Color(0x95a5a6))
                embed.add_field(name=f"Responsible Mod:", value=f"{cmduser.mention} ({cmduser.id})", inline=True)
                embed.add_field(name=f"Action Taken On:", value=f"{member.mention} ({member.id})", inline=True)
                embed.add_field(name=f"Reason:", value=f"{reason}", inline=False)
                embed.set_thumbnail(url=url)
                await mod_log_channel.send(embed=embed)
                await cmd.add_reaction("📜")
                return
    else:
        await cmduser.send(f"""You do not have permission to run that command! Context: `.ban`. \
You must have the role `Moderator` to run this command.""")
        await cmd.delete()
        return


@bot.command(pass_context=True, name="mute", aliases=["mu"])  # TODO ON ALL MUTES: Create role/give proper permissions
async def mute(ctx, member: discord.Member = None, *, reason: str = "Unspecified reason."):
    """Mutes a member permanently."""  # if no role named "Muted" exists
    cmd = ctx.message
    cmduser = ctx.message.author
    server = bot.get_guild(ctx.guild.id)
    user = server.get_member(ctx.author.id)
    moderator_role = discord.utils.get(server.roles, name="Moderator")
    muted_role = discord.utils.get(server.roles, name="Muted")
    mod_log_channel = discord.utils.get(server.channels, name="mod_log")
    url = member.avatar_url
    if moderator_role in user.roles:
        if member is None:
            await cmduser.send(f"Invalid member. To select a member, @mention them.")
            return
        elif muted_role is None:
            await cmduser.send(f"""The `Muted` role does not exist! Please create a role named `Muted`, \
and give it the proper permissions for this function to work properly.""")
            return
        elif moderator_role in member.roles:
            await cmduser.send(f"You cannot punish that user! They are a Moderator.")
            return
        else:
            if muted_role in member.roles:
                await cmduser.send("That member is already muted! Use `.unmute` to unmute them.")
                return
            else:
                await member.add_roles(muted_role)
                await cmd.add_reaction("👍")
                if mod_log_channel is None:
                    await cmduser.send(f"""Action successfully completed. To enable moderation command logging, \
please create a channel named `#mod_log`.""")
                    return
                else:
                    embed = discord.Embed(title=f"Mute created.", color=discord.Color(0x95a5a6))
                    embed.add_field(name=f"Responsible Mod:", value=f"{cmduser.mention} ({cmduser.id})", inline=True)
                    embed.add_field(name=f"Action Taken On:", value=f"{member.mention} ({member.id})", inline=True)
                    embed.add_field(name=f"Reason:", value=f"{reason}", inline=False)
                    embed.set_thumbnail(url=url)
                    await mod_log_channel.send(embed=embed)
                    await cmd.add_reaction("📜")
                    return
    else:
        await cmduser.send(f"""You do not have permission to run that command! Context: `.ban`. \
You must have the role `Moderator` to run this command.""")
        await cmd.delete()
        return


@bot.command(pass_context=True, name="purge_messages", aliases=["pm"])
async def purge_messages(ctx, member: discord.Member = None, amount: int = 1, *,
                         reason: str = "Unspecified reason."):
    """Searches through `amount` messages in channel in which command was invoked, deleting messages from `member`."""
    cmd = ctx.message
    cmduser = ctx.message.author
    server = bot.get_guild(ctx.guild.id)
    user = server.get_member(ctx.author.id)
    moderator_role = discord.utils.get(server.roles, name="Moderator")
    mod_log_channel = discord.utils.get(server.channels, name="mod_log")
    url = member.avatar_url
    if moderator_role in user.roles:
        if member is None:
            await cmduser.send(f"Invalid member. To select a member, @mention them.")
            return
        elif moderator_role in member.roles:
            await cmduser.send(f"You cannot punish that user! They are a Moderator.")
            return
        else:
            if amount < 1:
                await cmduser.send(f"Invalid amount. Amount must be a positive integer over 0.")
                return
            else:
                def is_member(message):
                    return message.author == member
                await cmd.channel.purge(limit=int(amount), check=is_member)
                await cmd.add_reaction("👍")
                if mod_log_channel is None:
                    await cmduser.send(f"""Action successfully completed. To enable moderation command logging, \
please create a channel named `#mod_log`.""")
                    return
                else:
                    embed = discord.Embed(title=f"Messages purged.", color=discord.Color(0x95a5a6))
                    embed.add_field(name=f"Responsible Mod:", value=f"{cmduser.mention} ({cmduser.id})", inline=True)
                    embed.add_field(name=f"Action Taken On:", value=f"{member.mention} ({member.id})", inline=True)
                    embed.add_field(name=f"Amount:", value=f"{amount}", inline=True)
                    embed.add_field(name=f"Reason:", value=f"{reason}", inline=False)
                    embed.set_thumbnail(url=url)
                    await mod_log_channel.send(embed=embed)
                    await cmd.add_reaction("📜")
                    return
    else:
        await cmduser.send(f"""You do not have permission to run that command! Context: `.ban`. \
You must have the role `Moderator` to run this command.""")
        await cmd.delete()
        return


@bot.command(pass_context=True, name="tempmute", aliases=["tm"])  # discord.utils.sleep_until
async def tempmute(ctx, member: discord.Member = None, duration: str = "1m", *, reason: str = "Unspecified reason."):
    """Temporarily mutes a member for the duration in minutes."""  # Do research on sleep_until!
    """Note: For now, member remains muted if bot is restarted before duration expires. Use `.unmute`."""
    cmd = ctx.message
    cmduser = ctx.message.author
    server = bot.get_guild(ctx.guild.id)
    user = server.get_member(ctx.author.id)
    moderator_role = discord.utils.get(server.roles, name="Moderator")
    temp_muted_role = discord.utils.get(server.roles, name="Temp. Muted")
    muted_role = discord.utils.get(server.roles, name="Muted")
    mute_duration = re.search(r"(^\d{1,2})(m$|h$|d$)", duration, re.IGNORECASE)
    mute_duration_number = int(mute_duration.group(1))
    mute_duration_letter = str(mute_duration.group(2))
    final_mute_duration_number = 0
    time_longevity_signifier = "minute(s)"
    mod_log_channel = discord.utils.get(server.channels, name="mod_log")
    url = member.avatar_url
    if moderator_role in user.roles:
        if member is None:
            await cmduser.send(f"Invalid member. To select a member, @mention them.")
            return
        elif moderator_role in member.roles:
            await cmduser.send(f"You cannot punish that user! They are a Moderator.")
            return
        else:
            if temp_muted_role is None:
                await cmduser.send(f"""The `Temp. Muted` role does not exist! Please create a role named \
`Temp. Muted`, and give it the proper permissions for this function to work properly.""")
                return
            elif temp_muted_role in member.roles:
                await cmduser.send(f"That member is already temporarily muted! Use `.unmute` to unmute them.")
                return
            elif muted_role in member.roles:
                await cmduser.send(f"That member is already permanently muted! Use `.unmute` to unmute them.")
                return
            else:
                if mute_duration_letter is "m":
                    final_mute_duration_number = mute_duration_number * 60
                    time_longevity_signifier = "minute(s)"
                    pass
                elif mute_duration_letter is "h":
                    final_mute_duration_number = mute_duration_number * 3600
                    time_longevity_signifier = "hour(s)"
                    pass
                elif mute_duration_letter is "d":
                    final_mute_duration_number = mute_duration_number * 86400
                    time_longevity_signifier = "day(s)"
                    pass
                await member.add_roles(temp_muted_role)
                await cmd.add_reaction("👍")
                if mod_log_channel is None:
                    await cmduser.send(f"""Action successfully completed. To enable moderation command logging, \
please create a channel named `#mod_log`.""")
                    pass
                else:
                    embed = discord.Embed(title=f"Temporary mute created.", color=discord.Color(0x95a5a6))
                    embed.add_field(name=f"Responsible Mod:", value=f"{cmduser.mention} ({cmduser.id})", inline=True)
                    embed.add_field(name=f"Action Taken On:", value=f"{member.mention} ({member.id})", inline=True)
                    embed.add_field(name=f"Duration:`*`", value=f"""{mute_duration_number} \
{time_longevity_signifier}.""", inline=True)
                    embed.add_field(name=f"Reason:", value=f"{reason}", inline=False)
                    embed.set_footer(text=f"""*: Due to current programming limitations, temporary mutes \
may last indefinitely if the bot restarts between mute set point and end point. Please use \
`.unmute` if this situation arises. Many apologies.""")
                    embed.set_thumbnail(url=url)
                    await mod_log_channel.send(embed=embed)
                    await cmd.add_reaction("📜")
                    pass
                await asyncio.sleep(final_mute_duration_number)
                await member.remove_roles(temp_muted_role)
                await cmduser.send(f"""I have unmuted {member} after waiting {mute_duration_number} \
{time_longevity_signifier}.""")
                return
    else:
        await cmduser.send(f"""You do not have permission to run that command! Context: `.ban`. \
You must have the role `Moderator` to run this command.""")
        await cmd.delete()
        return


@bot.command(pass_context=True, name="unban", aliases=["ub"])
async def unban(ctx, member_id: int = None, reason: str = None):
    """Unbans a user from a server via ID."""
    cmd = ctx.message
    cmduser = ctx.message.author
    server = bot.get_guild(ctx.guild.id)
    user = server.get_member(ctx.author.id)
    moderator_role = discord.utils.get(server.roles, name="Moderator")
    mod_log_channel = discord.utils.get(server.channels, name="mod_log")
    url = member.avatar_url
    if moderator_role in user.roles:
        if member_id is None:
            await cmduser.send(f"Invalid member. To select a member, use their ID.")
            return
        else:
            to_unban = await bot.fetch_user(member_id)
            banned = await cmd.guild.bans()
            banned_list = str(banned)
            is_banned = re.search(rf"{member_id}", banned_list)
            if is_banned is None:
                await cmduser.send(f"That user is not banned! User: {to_unban} ({member_id}.")
                return
            else:
                if reason is None:
                    await cmduser.send(f"Please specify a reason for the unban.")
                    return
                else:
                    await cmd.guild.unban(to_unban)
                    await cmd.add_reaction("👍")
                    if mod_log_channel is None:
                        await cmduser.send(f"""Action successfully completed. To enable moderation command logging, \
please create a channel named `#mod_log`.""")
                        return
                    else:
                        embed = discord.Embed(title=f"Unban occurred.", color=discord.Color(0x95a5a6))
                        embed.add_field(name=f"Responsible Mod:",
                                        value=f"{cmduser.mention} ({cmduser.id})", inline=True)
                        embed.add_field(name=f"Action Taken On:", value=f"{member_id}", inline=True)
                        embed.add_field(name=f"Reason:", value=f"{reason}", inline=False)
                        embed.set_thumbnail(url=url)
                        await mod_log_channel.send(embed=embed)
                        await cmd.add_reaction("📜")
                        return
    else:
        await cmduser.send(f"""You do not have permission to run that command! Context: `.ban`. \
You must have the role `Moderator` to run this command.""")
        await cmd.delete()
        return


@bot.command(pass_context=True, name="unmute", aliases=["um"])
async def unmute(ctx, member: discord.Member = None, *, reason: str = "Unspecified reason."):
    """Unmutes a temporarily or permanently muted member."""
    cmd = ctx.message
    cmduser = ctx.message.author
    server = bot.get_guild(ctx.guild.id)
    user = server.get_member(ctx.author.id)
    moderator_role = discord.utils.get(server.roles, name="Moderator")
    muted_role = discord.utils.get(server.roles, name="Muted")
    temp_muted_role = discord.utils.get(server.roles, name="Temp. Muted")
    mod_log_channel = discord.utils.get(server.channels, name="mod_log")
    url = member.avatar_url
    if moderator_role in user.roles:
        if member is None:
            await cmduser.send(f"Invalid member. To select a member, @mention them.")
            return
        elif moderator_role in member.roles:
            await cmduser.send(f"You cannot un-punish that user! They are a Moderator.")
            return
        else:
            if muted_role or temp_muted_role in member.roles:
                if muted_role in member.roles:
                    await member.remove_roles(muted_role)
                    pass
                elif temp_muted_role in member.roles:
                    await member.remove_roles(temp_muted_role)
                    pass
                await cmd.add_reaction("👍")
                if mod_log_channel is None:
                    await cmduser.send(f"""Action successfully completed. To enable moderation command logging, \
please create a channel named `#mod_log`.""")
                    return
                else:
                    embed = discord.Embed(title=f"Unmute initiated.", color=discord.Color(0x95a5a6))
                    embed.add_field(name=f"Responsible Mod:", value=f"{cmduser.mention} ({cmduser.id})", inline=True)
                    embed.add_field(name=f"Action Taken On:", value=f"{member.mention} ({member.id})", inline=True)
                    embed.add_field(name=f"Reason:", value=f"{reason}", inline=False)
                    embed.set_thumbnail(url=url)
                    await mod_log_channel.send(embed=embed)
                    await cmd.add_reaction("📜")
                    return
            else:
                await cmduser.send(f"That member is not muted! Use `.mute` or `.tempmute` to mute them.")
                return
    else:
        await cmduser.send(f"""You do not have permission to run that command! Context: `.ban`. \
You must have the role `Moderator` to run this command.""")
        await cmd.delete()
        return


@bot.command(pass_context=True, name="warn", aliases=["w"])  # TODO: Unfinished. Unsure how to count warns.
async def warn(ctx, member: discord.Member = None, *, reason: str = "Unspecified reason."):  # FOR WARN INFO:
    """Gives a user a warning."""  # Have add_field loop for every entry under warn reason and time
    cmd = ctx.message
    cmduser = ctx.message.author
    server = bot.get_guild(ctx.guild.id)
    user = server.get_member(ctx.author.id)
    moderator_role = discord.utils.get(server.roles, name="Moderator.")
    mod_log_channel = discord.utils.get(server.channels, name="mod_log")
    url = member.avatar_url
    tz_utc = pytz.timezone("UTC")
    current_utc_time = datetime.now(tz_utc)
    if moderator_role in ctx.author.roles:
        with open("warn_file.json", "r+") as warn_file:
            check_if_id_in_reason = re.search(r"\d{18}", str(reason), re.IGNORECASE)
            if member is None:
                await ctx.send("Please specify a member. You can do this by @mentioning them.")
                return
            elif member is not None:
                pass
            if check_if_id_in_reason is None:
                pass
            elif check_if_id_in_reason is not None:
                await ctx.send("Please do not include user or server IDs in a warn reason.")
                return
            warn_file_content = json.load(warn_file)
            print(warn_file_content)
            server_search = re.search(rf"({server.id})", str(warn_file_content))
            server_warned_members = warn_file_content["warn_list"][f"{server.id}"]
            print(server_search)
            print(server_warned_members)  # TODO: This whole thing bugs the fuck out if someone's id is in the reason
            if server_search is not None:
                pass
            elif server_search is None:
                new_server_id = {
                    f"{server.id}": {

                    }
                }
                with open("warn_file.json", "r+") as warn__file:
                    data2 = json.load(warn__file)
                    data2["warn_list"].update(new_server_id)
                    warn__file.seek(0)
                    json.dump(data2, warn__file, indent=2)
                    warn__file.truncate()
                    warn__file.close()
                    print("ass")
                    pass
            if str(member.id) in str(server_warned_members):  # Working on this
                with open("warn_file.json", "r+") as warn___file:
                    data3 = json.load(warn___file)
                    current_warn_count = []
                    current_warn_count = data3["warn_list"][f"{ctx.guild.id}"][f"{member.id}"]["warn_count"]
                    print("9")
                    new_warn_count = int(current_warn_count) + 1
                    print("a23")
                    print(str(new_warn_count))
                    new_warn = {
                        "warn_count": f"{str(new_warn_count)}"
                    }
                    new_warn_reason_and_time = {
                        f"{str(new_warn_count)}": f"""\
{reason} | {current_utc_time.strftime("%m/%d/%Y @ %I:%M:%S %p %Z")}"""
                    }
                    with open("warn_file.json", "r+") as warn_____file:
                        data5 = json.load(warn_____file)
                        print("ba")
                        data5["warn_list"][f"{server.id}"][f"{member.id}"].update(new_warn)
                        print("ca")
                        warn_____file.seek(0)
                        print("da")
                        json.dump(data5, warn_____file, indent=2)
                        warn_____file.truncate()
                        warn_____file.close()
                        print("assa")
                        with open("warn_file.json", "r+") as warn______file:
                            data6 = json.load(warn______file)
                            data6["warn_list"][f"{server.id}"][f"{member.id}"]["warn_reason_and_time"].update(
                                new_warn_reason_and_time
                            )
                            warn______file.seek(0)
                            json.dump(data6, warn______file, indent=2)
                            warn______file.truncate()
                            warn______file.close()
                            pass
                        await cmd.add_reaction("👍")
                        if mod_log_channel is None:
                            await cmduser.send(f"""Action successfully completed. To enable moderation command logging, \
please create a channel named `#mod_log`.""")
                            return
                        else:
                            embed = discord.Embed(title=f"Warn issued.", color=discord.Color(0xd47006))
                            embed.add_field(name=f"Responsible Mod:", value=f"{cmduser.mention} ({cmduser.id})",
                                            inline=True)
                            embed.add_field(name=f"Action Taken On:", value=f"{member.mention} ({member.id})",
                                            inline=True)
                            embed.add_field(name=f"Warn Count:", value=f"{str(new_warn_count)}.", inline=True)
                            embed.add_field(name=f"Reason:", value=f"{reason}", inline=False)
                            embed.set_footer(text=f"""
Warn Issued At: {current_utc_time.strftime("%m/%d/%Y @ %I:%M:%S %p %Z")}""")
                            embed.set_thumbnail(url=url)
                            await mod_log_channel.send(embed=embed)
                            await cmd.add_reaction("📜")
                            return
            elif str(member.id) not in str(server_warned_members):
                print("a")
                tz_utc = pytz.timezone("UTC")
                current_utc_time = datetime.now(tz_utc)
                new_member_id = {
                    f"{member.id}": {

                    }
                }
                with open("warn_file.json", "r+") as warn__A__file:
                    dataA = json.load(warn__A__file)
                    dataA["warn_list"][f"{server.id}"].update(new_member_id)
                    warn__A__file.seek(0)
                    json.dump(dataA, warn__A__file, indent=2)
                    warn__A__file.truncate()
                    warn__A__file.close()
                    pass
                initial_warn = {
                    "warn_count": "1",
                    "warn_reason_and_time": {
                        "1": f"""{reason} | {current_utc_time.strftime("%m/%d/%Y @ %I:%M:%S %p %Z")}"""
                    }
                }
                print("a2")
                with open("warn_file.json", "r+") as warn____file:
                    data4 = json.load(warn____file)
                    print("b")
                    data4["warn_list"][f"{server.id}"][f"{member.id}"].update(initial_warn)
                    print("c")
                    warn____file.seek(0)
                    print("d")
                    json.dump(data4, warn____file, indent=2)
                    warn____file.truncate()
                    warn____file.close()
                    print("ass")
                    print(warn_file_content)
                    await cmd.add_reaction("👍")
                    if mod_log_channel is None:
                        await cmduser.send(f"""Action successfully completed. To enable moderation command logging, \
please create a channel named `#mod_log`.""")
                        return
                    else:
                        embed = discord.Embed(title=f"Warn issued.", color=discord.Color(0xd47006))
                        embed.add_field(name=f"Responsible Mod:", value=f"{cmduser.mention} ({cmduser.id})",
                                        inline=True)
                        embed.add_field(name=f"Action Taken On:", value=f"{member.mention} ({member.id})", inline=True)
                        embed.add_field(name=f"Warn Count:", value="1.", inline=True)
                        embed.add_field(name=f"Reason:", value=f"{reason}", inline=False)
                        embed.set_footer(text=f"""
Warn Issued At: {current_utc_time.strftime("%m/%d/%Y @ %I:%M:%S %p %Z")}""")
                        embed.set_thumbnail(url=url)
                        await mod_log_channel.send(embed=embed)
                        await cmd.add_reaction("📜")
                        return
    else:
        await cmduser.send(f"You do not have permission to run that command! Context: `.warn`.")
        await cmd.delete()
        return


@bot.command(pass_context=True, name="warn_list", aliases=["wl", "w_l"])
async def warn_list(ctx, member: discord.Member = None, *, reason_number: int = None):
    print("what")
    """Views the list of a member's warnings."""
    moderator_role = discord.utils.get(ctx.guild.roles, name="Moderator.")
    mod_log_channel = discord.utils.get(ctx.guild.channels, name="mod_log")
    url = member.avatar_url
    print("a")
    if moderator_role not in ctx.author.roles:
        print("b")
        await ctx.author.send(f"You do not have permission to run that command! Context: `.warn_list`.")
        await ctx.message.delete()
        return
    elif moderator_role in ctx.author.roles:
        print("c1")
        if member is None:
            await ctx.send("Please select a member to view the warn log of. To select a member, @mention them.")
            return
        elif member is not None:
            pass
        if reason_number is None:
            print("g")
            pass
        elif reason_number is not None:
            print("h")
            pass
        print("c")
        with open("warn_file.json", "r") as warn_list:
            print("d")
            data = json.load(warn_list)
            print("e")
            warn_count = data["warn_list"][f"{ctx.guild.id}"][f"{member.id}"]["warn_count"]
            embed = discord.Embed(title="Warns List:", color=discord.Color(0xd47006))
            print("f")
            embed.add_field(name="Member:", value=f"{member.mention}\n({member.id})", inline=True)
            embed.add_field(name="Warn Count:", value=f"{str(warn_count)}", inline=True)
            embed.set_thumbnail(url=url)
            await ctx.send(embed=embed)
            return




# Owner Only


@bot.command(pass_context=True, name="changenick", aliases=["chn", "nick"])
async def changenick(ctx, *args):
    """Changes the bot's nickname on the server the command is invoked on."""
    cmd = ctx.message
    cmduser = ctx.message.author
    if ctx.author.id != 97153790897045504:
        await cmduser.send(f"You do not have permission to run that command! Context: `.changenick`.")
        await cmd.delete()
        return
    else:
        name = " ".join(args)
        await ctx.guild.get_member(bot.user.id).edit(nick=name)
        await cmd.add_reaction("👍")
        return


@bot.group(pass_context=True, name="changepresence", aliases=["chp"])
async def changepresence(ctx, *, presence: str = None):
    """Changes presence."""
    cmd = ctx.message
    cmduser = ctx.message.author
    if ctx.author.id != 97153790897045504:
        await cmduser.send(f"You do not have permission to run that command! Context: `.changepresence`.")
        await cmd.delete()
        return
    else:
        if presence is None:
            await bot.change_presence(status=discord.Status.online, activity=discord.Game("w/ batty friends! | .help"))
            return
        else:
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"{presence} | .help"))
            return


@bot.command(pass_context=True)
async def de(ctx, *args):
    """Echoes back what you say while deleting invocation for illusion of sentience."""
    cmd = ctx.message
    cmduser = ctx.message.author
    if ctx.author.id != 97153790897045504:
        await cmduser.send(f"You do not have permission to use that command! Context: `.de`.")
        await cmd.delete()
        return
    else:
        await ctx.send(" ".join(args))
        await cmd.delete()
        return


@bot.command(pass_context=True, name="questembed", aliases=["qe"])
async def questembed(ctx, title: str = None, color: str = None, field_title: str = None, field_text: str = None,
                     footer: str = None, thumbnail: str = None):
    """Creates a quest embed for Elysium."""
    cmd = ctx.message
    cmduser = ctx.message.author
    if ctx.author.id != 97153790897045504:
        await cmduser.send(f"You do not have permission to use that command! Context: `.questembed`.")
        await cmd.delete()
        return
    else:
        embed = discord.Embed(title=title, color=discord.Color(int(color, 16)))
        embed.add_field(name=field_title, value=field_text)
        embed.set_footer(text=footer)
        embed.set_thumbnail(url=thumbnail)
        await ctx.send(embed=embed)
        await cmd.delete()
        return


@bot.command(pass_context=True)
async def invite(ctx):
    """Prints an invite link for Batty Bot."""
    cmd = ctx.message
    cmduser = ctx.message.author
    invitelink = os.environ.get("Batty_Bot_Invite")
    if ctx.author.id != 97153790897045504:
        await cmduser.send(f"You do not have permission to run that command! Context: `.invite`.")
        await cmd.delete()
        return
    else:
        await cmduser.send(f"{invitelink}")
        await cmd.add_reaction("👍")
        return


@bot.command(pass_context=True)
async def leave(ctx, server: int = None):
    """Leaves a server by ID."""
    cmd = ctx.message
    cmduser = ctx.message.author
    if ctx.author.id != 97153790897045504:
        await cmduser.send(f"You do not have permission to run that command! Context: `.leave`.")
        await cmd.delete()
        return
    else:
        if server is None:
            to_leave = bot.get_guild(ctx.guild.id)
            await cmduser.send(f"I have left {cmd.guild.name} ({cmd.guild.id}).")
            await to_leave.leave()
            return
        else:
            to_leave = bot.get_guild(server)
            await cmduser.send(f"I have left {to_leave.name} ({to_leave.id}).")
            await to_leave.leave()
            return


@bot.command(pass_context=True)
async def purge(ctx, amount):
    """Purges bot messages, looking back `amount` amount of messages (including invocation)."""
    cmd = ctx.message
    cmduser = ctx.message.author
    if ctx.author.id != 97153790897045504:
        await cmduser.send(f"You do not have permission to run that command! Context: `.purge`.")
        await cmd.delete()
        return
    else:
        def is_batty(message):
            return message.author.id == 635484274023465000
        await ctx.channel.purge(limit=int(amount), check=is_batty)
        await ctx.message.add_reaction("👍")
        return


# Unfinished or For Testing | I wonder if this'll ever get done lmao


# @bot.command(pass_context=True, name="crps", aliases=["challengerockpaperscissors"])
# async def crps(ctx, player2: discord.User, move):
    # embed = discord.Embed(title="A challenge!", color=discord.Color(0xe0890d), description=f"""{player2.mention}!
    # You have been challenged to a Rock Paper Scissors match by {ctx.message.author.mention}! Do you accept?""")
    # embed.set_thumbnail(url="""
    # https://cdn.discordapp.com/attachments/627784999873019914/645061608976154665/challenger.png""")
    # embed.set_footer(text="""If you do, simply say what move you wish to make! If not, just reply "no".""")
    # embed2 = await ctx.send(embed=embed)
    # await embed2.add_reaction(emoji="\N{THUMBS UP SIGN}")
    # await ctx.message.delete()
#
    # def check(user):
    #     return user == player2
#
    # await bot.wait_for("reaction_add", check=check)
    # await ctx.send(f"{player2.mention}, {move}")


# On Message


@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    batty = 635484274023465000
    repeat = "__***FULLMETAL ALCHEMIST.***__\n"
    cnt = message.content.lower()
    two = re.search(r"(2|two)!$", cnt)
    donotemote = re.search(r":.*?(pog|monka).*?:", cnt)
    donotemote2 = re.search(r"^(\.)e", cnt)
    monka = "monka"
    pog = "pog"
    if message.author.id != batty:
        out = ""
        if "fullmetal alchemist" in cnt:
            out += repeat
        if "/shrug" in cnt:
            out += "¯\\_(ツ)_/¯\n"
        if monka or pog in cnt:
            if donotemote:
                return
            if donotemote2:
                pass
            else:
                if monka in cnt:
                    await ctx.send("<:monkas:636575202217689099>")
                if pog in cnt:
                    await ctx.send("<:pogchamp:636572402054201368>")
        if message.content.startswith(".."):
            return
        if two:
            image = "assets/2.gif"
            await ctx.send(file=discord.File(image))
        if out:
            await ctx.send(out)
        if message.author.id == 97153790897045504 and message.content.startswith("Batty!"):
            await ctx.message.add_reaction("👍")
        if message.author.id == 461265486655520788 and message.channel.id != 414890945243512842:
            await ctx.message.delete()
        await bot.process_commands(message)


# TODO: Completed in current build:
# `.roll` now works if D is capitalized

# TODO: MODERATION TODO
# ZHU WISHLIST: Warn logging, temp muting/banning, case tracking per user, username/nick tracking, raid mode

# GENERAL TODO:
# FIgure out if you can get a list of EVERYBODY in a role
# Create TempMuted role?
# For unmute, like, do if member not in muted or temp muted do thing. If member muted or temp muted cannot mute

# After MODERATION suite:
# 100% total rewrite. You've learned so much since the beginning, and now it's time to make this shit more readable.

# TODO: IF TEMPMUTE/BAN EXPIRATION PAST FLOW:
# event looping every 30 seconds
# ignored_variable = 1
# while ignored_variable == 1
# if temp expiration is inpast:
# remove role/unban
# else:
# pass
# asyncio.sleep(30)

# TODO: Later
# TODO: Modifiers on roll?

# TODO: Undefined
# TODO: Figure out how to store numbers that are linked to userid in a text doc or smth to recall at any time, cookies
# TODO: Challenge RPS
# TODO: Add Challenge RPS to help
# TODO: Birthday calender?
# TODO: Schedule tasks for specific days
# TODO: Birthday calender print is formatted table, reactions to navigate months
# TODO: Voice??? Maybe???? Make Patreon exclusive


# TODO: Long Way Off, hold 0 hope that these will ever happen
# TODO: Voice?


bot.run(TOKEN)
