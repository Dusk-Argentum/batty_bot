# import asyncio ### It SAYS this is unused, but I use it... a lot... so I'm leaving it here, commented, just in case.
import os

import discord
from discord.ext import commands
from discord.ext.commands import CommandInvokeError
from discord.ext.commands import CommandNotFound


import random
import re


OWNER_ID = "97153790897045504"  # Hehe, that's me!


PREFIX = "."
DESCRIPTION = "A bot made custom for Gazia's Bat Den. Just your typical chat bot! Made by Dusk-Argentum#6530."
TOKEN = os.environ.get("BBR")


bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), description=DESCRIPTION, pm_help=False,
                   case_insensitive=True)
client = discord.Client()  # Leave this alone. I barely understand what this does, sometimes.


bot.remove_command("help")


# Events


@bot.event
async def on_ready():
    # greetings_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    # gamers_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    # socialists_role_message = await bot.get_channel(636366607626666014).fetch_message(636367012372676609)
    # await greetings_role_message.add_reaction(emoji="👋")
    # await gamers_role_message.add_reaction(emoji="🎮")
    # await socialists_role_message.add_reaction(emoji="🗣") ### Leave these in, in case of emergency, I guess.
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("w/ batty friends! | .help"))


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
    if ctx.guild.id == 290304276381564928:
        welcome_channel = bot.get_channel(290304276381564928)
        await welcome_channel.send(f"""<@&636374013731667969>, {ctx.mention}!
        Welcome to Gazia's Bat Den! Please read <#413876271865528320>, and enjoy your stay!""")
    else:
        print("Unexpected.")


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


# Help


@bot.group(pass_context=True, name="help2", aliases=["cmds", "commands", "h", "h-hewp!!!", "help"])
async def help2(ctx):
    """The help command."""
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
        embed.add_field(name="General", value="""`.help` \n Shows this help. \n `.test` 
        Sends a test message to check if the bot's online.""", inline=True)
        embed.add_field(name="Roles", value="""`.role [subcommand]` 
        Assign or redact a specific role from yourself via command.""", inline=False)
        embed.add_field(name="Fun", value="""`.eightball`
        Gives a cryptic answer to your queries. \n `.emoji [subcommand]`
        Have the bot print out a specific emoji. \n `.meme`
        Have the bot print out a specific meme. \n `.rps [move]`
        Play Rock, Paper, Scissors with the bot. \n `.roll` \n Rolls dice. Format: `x`d`y`, ex. 2d6.
        `.simpleroll` \n Simply chooses a random number between 1 and your input.""", inline=True)
        embed.add_field(name="Meta", value="""`.bug [name] [description]` \n Submit a bug report to the dev.
        `.suggestion [name] [description]` \n Submit a suggestion to the dev.""", inline=True)
        embed.add_field(name="Key Phrases", value="""`Fullmetal Alchemist`
        Causes the bot to repeat the phrase, but louder.
        `/shrug` \n Prints "¯\\_(ツ)_/¯", no matter where `/shrug` is in your message.
        `2!` at the end \n Sends the "Peggle! 2!" gif.""", inline=True)
        embed.set_footer(text="""If a command has subcommands,
        do `.help [command name]` for further help. Made by Dusk-Argentum#6530!""")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
        await ctx.send(embed=embed)
    else:
        pass


@help2.command(pass_context=True, name="-pm")
async def pm(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
    embed.add_field(name="General", value="""`.help` \n Shows this help. \n `.test` 
    Sends a test message to check if the bot's online.""", inline=True)
    embed.add_field(name="Roles", value="""`.role [subcommand]` 
    Assign or redact a specific role from yourself via command.""", inline=False)
    embed.add_field(name="Fun", value="""`.eightball`
    Gives a cryptic answer to your queries. \n `.emoji [subcommand]`
    Have the bot print out a specific emoji. \n `.meme`
    Have the bot print out a specific meme. \n `.rps [move]`
    Play Rock, Paper, Scissors with the bot. \n `.roll` \n Rolls dice. Format: `x`d`y`, ex. 2d6.
    `.simpleroll` \n Simply chooses a random number between 1 and your input.""", inline=True)
    embed.add_field(name="Meta", value="""`.bug [name] [description]` \n Submit a bug report to the dev.
            `.suggestion [name] [description]` \n Submit a suggestion to the dev.""", inline=True)
    embed.add_field(name="Key Phrases", value="""`Fullmetal Alchemist`
    Causes the bot to repeat the phrase, but louder.
    `/shrug` \n Prints "¯\\_(ツ)_/¯", no matter where `/shrug` is in your message.
    `2!` at the end \n Sends the "Peggle! 2!" gif.""", inline=True)
    embed.set_footer(text="""If a command has subcommands,
    do `.help [command name]` for further help. Made by Dusk-Argentum#6530!""")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.author.send(embed=embed)


@help2.group(pass_context=True, name="help3", aliases=["cmds", "commands", "h", "h-hewp!!!", "help"])
async def help3(ctx):  # Wish everything named help didn't "shadow builtin command"!
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE9B52A), description="""Aliases: 
    `.cmds`, `.commands`, `.h`, `.h-hewp!!!`.""")
        embed.add_field(name="`.help`", value="Shows the help for Batty Bot.", inline=True)
        embed.add_field(name="Possible Arguments", value="""`-pm` \n PMs the help to you,
        instead of posting it in the invoking channel.""", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
        await ctx.send(embed=embed)
    else:
        pass


@help3.command(pass_context=True, name="-pm")
async def pm(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE9B52A), description="""Aliases: 
        `.cmds`, `.commands`, `.h`, `.h-hewp!!!`.""")
    embed.add_field(name="`.help`", value="Shows the help for Batty Bot.", inline=True)
    embed.add_field(name="Possible Arguments", value="""`pm` \n PMs the help to you,
    instead of posting it in the invoking channel.""", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.author.send(embed=embed)


@help2.group(pass_context=True)
async def test(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE9B52A))
        embed.add_field(name="`.test`", value="Sends a test message to check if the bot's online.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
        await ctx.send(embed=embed)
    else:
        pass


@test.command(pass_context=True, name="-pm")
async def pm(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE9B52A))
    embed.add_field(name="`.test`", value="Sends a test message to check if the bot's online.", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.author.send(embed=embed)


@help2.group(pass_context=True)
async def role(ctx):
    if ctx.invoked_subcommand is None:
        """Help for `.role`."""
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
        embed.add_field(name="`.role`", value="""Assign or redact a specific role from yourself via command.""",
                        inline=True)
        embed.add_field(name="Possible Arguments", value="""`gamers` \n  Assigns or redacts the Gamers role from you.
        `greetings` \n Assigns or redacts the Greetings role from you. \n `socialists` \n Assigns or redacts the
        Socialists role from you.""")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
        await ctx.send(embed=embed)
    else:
        pass


@role.command(pass_context=True, name="-pm")
async def pm(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
    embed.add_field(name="`.role`", value="Assign or redact a specific role from yourself via command.", inline=True)
    embed.add_field(name="Possible Arguments", value="""`gamers` \n  Assigns or redacts the Gamers role from you.
            `greetings` \n Assigns or redacts the Greetings role from you. \n `socialists` \n Assigns or redacts the
            Socialists role from you.""")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.author.send(embed=embed)


@help2.group(pass_context=True, aliases=["8", "8ball"])
async def eightball(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
        `.8`, `.8ball`.""")
        embed.add_field(name="`.eightball`", value="Gives a cryptic answer to your queries.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
        await ctx.send(embed=embed)
    else:
        pass


@eightball.command(pass_context=True, name="-pm")
async def pm(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
            `.8`, `.8ball`.""")
    embed.add_field(name="`.eightball`", value="Gives a cryptic answer to your queries.")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.author.send(embed=embed)


@help2.group(pass_context=True, aliases=["e"])
async def emoji(ctx):
    if ctx.invoked_subcommand is None:
        """Help for `.emoji`."""
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
        embed.add_field(name="`.emoji`", value="""Have the bot print out a specific emoji.""", inline=True)
        embed.add_field(name="Accepted Arguments", value="""`monkas` \n Sends monkaS. \n `pikachu`
        Sends Surprised Pikachu, in the style of the Poketch. \n `pogchamp` \n Sends Pogchamp.""")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
        await ctx.send(embed=embed)
    else:
        pass


@emoji.command(pass_context=True, name="-pm")
async def pm(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
    embed.add_field(name="`.emoji`", value="""Have the bot print out a specific emoji.""", inline=True)
    embed.add_field(name="Accepted Arguments", value="""`monkas` \n Sends monkaS. \n `pikachu`
            Sends Surprised Pikachu, in the style of the Poketch. \n `pogchamp` \n Sends Pogchamp.""")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.author.send(embed=embed)


@help2.group(pass_context=True, aliases=["m"])
async def meme(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
        `.m`.""")
        embed.add_field(name="`.meme`", value="Send a specific meme.", inline=True)
        embed.add_field(name="Accepted Arguments", value="""`typo` \n Sends the "TYPO! In the Groupchat" meme.
        `wig` \n Sends the "Wig" meme. \n `wig2` \n Sends a "Wig" video clip.""")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
        await ctx.send(embed=embed)
    else:
        pass


@meme.group(pass_context=True, name="-pm")
async def pm(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
            `.m`.""")
    embed.add_field(name="`.meme`", value="Send a specific meme.", inline=True)
    embed.add_field(name="Accepted Arguments", value="""`typo` \n Sends the "TYPO! In the Groupchat" meme.
    `wig` \n Sends the "Wig" meme. \n `wig2` \n Sends a "Wig" video clip.""")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.author.send(embed=embed)


@help2.group(pass_context=True, aliases=["rockpaperscissors"])
async def rps(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
        `.rockpaperscissors`.""")
        embed.add_field(name="`.rps`", value="Play Rock, Paper, Scissors with the bot.", inline=True)
        embed.add_field(name="Accepted Arguments", value="""`rock` \n Play as Rock. \n `paper`
        Play as Paper. \n `scissors` \n Play as scissors.""")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
        await ctx.send(embed=embed)
    else:
        pass


@rps.group(pass_context=True, name="-pm")
async def pm(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
            `.rockpaperscissors`.""")
    embed.add_field(name="`.rps`", value="Play Rock, Paper, Scissors with the bot.", inline=True)
    embed.add_field(name="Accepted Arguments", value="""`rock` \n Play as Rock. \n `paper`
            Play as Paper. \n `scissors` \n Play as scissors.""")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.author.send(embed=embed)


@help2.group(pass_context=True, aliases=["r"])
async def roll(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
        `.r`.""")
        embed.add_field(name="`.roll`", value="Rolls dice. Format: `x`d`y`, ex. 2d6.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
        await ctx.send(embed=embed)
    else:
        pass


@roll.group(pass_context=True, name="-pm")
async def pm(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
            `.r`.""")
    embed.add_field(name="`.roll`", value="Rolls dice. Format: `x`d`y`, ex. 2d6.", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.author.send(embed=embed)


@help2.group(pass_context=True, aliases=["sr"])
async def simpleroll(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
        `.sr`.""")
        embed.add_field(name="`.simpleroll`", value="""Simply chooses a random number between 1 and your input.""",
                        inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
        await ctx.send(embed=embed)
    else:
        pass


@simpleroll.command(pass_context=True, name="-pm")
async def pm(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
            `.sr`.""")
    embed.add_field(name="`.simpleroll`", value="Simply chooses a random number between 1 and your input.", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.author.send(embed=embed)


@help2.group(pass_context=True, name="bug")
async def bug(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
        `.b`.""")
        embed.add_field(name="`.bug", value="Submit a bug report to the dev.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
        await ctx.send(embed=embed)
    else:
        pass


@bug.command(pass_context=True, name="-pm")
async def pm(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
            `.b`.""")
    embed.add_field(name="`.bug", value="Submit a bug report to the dev.", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.author.send(embed=embed)


@help2.group(pass_context=True, name="suggestion")
async def suggestion(ctx):
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
        `.s`, `.suggest`.""")
        embed.add_field(name="`.suggestion", value="Submit a suggestion to the dev.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
        await ctx.send(embed=embed)
    else:
        pass


@suggestion.command(pass_context=True, name="-pm")
async def pm(ctx):
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A), description="""Aliases:
            `.s`, `.suggestion`.""")
    embed.add_field(name="`.suggestion", value="Submit a suggestion to the dev.", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.author.send(embed=embed)

# General


@bot.command(pass_context=True, name="test", hidden=True)  # Basically, confirm that the bot is still online.
async def test(ctx):
    """ Confirms whether or not the bot is online, basically. """
    await ctx.send("I work!")


# Role


@bot.group(pass_context=True, name="role")
async def role(ctx):
    """Adds or removes a role."""
    if ctx.invoked_subcommand is None:
        await ctx.send("Please choose a role. Valid roles: `Gamers`, `Greetings`, and `Socialists`.")


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
    else:
        await ctx.author.add_roles(greetings_role)
        await(await ctx.send(f"OK, {ctx.author.mention}! You're now a part of the Greetings role!")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)


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
    else:
        await ctx.author.add_roles(gamers_role)
        await(await ctx.send(f"OK, {ctx.author.mention}! You're now a part of the Gamers role!")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)


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
    else:
        await ctx.author.add_roles(socialists_role)
        await(await ctx.send(f"OK, {ctx.author.mention}! You're now a part of the Socialists role!")).delete(
            delay=15)
        await message.add_reaction(emoji="\N{THUMBS UP SIGN}")
        await message.delete(delay=15)


# Fun


# TODO


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


@bot.command(pass_context=True, name="eightball", aliases=["8", "8ball"])
async def eightball(ctx):
    """Gives a cryptic answer to your queries."""
    answer = random.choice(["Yes.", "No.", "Possibly.", "Not likely.", "It's up to you.", "It's out of your control.",
                            "I can't say.", "That is beyond the scope of my programming."])
    await ctx.send(answer)


@bot.group(pass_context=True, name="emoji", aliases=["e", "emote"])
async def emoji(ctx):
    """Prints a specific emoji."""
    if ctx.invoked_subcommand is None:
        await ctx.send("Please enter a valid emoji. Valid emojis: `monkas`, `pogchamp`, `pikachu`.")
    else:
        return


@emoji.command(pass_context=True, name="pogchamp", aliases=["pog", "po"])
async def pogchamp(ctx):
    # await ctx.send(f"{ctx.author.mention} says: <:pogchamp:636572402054201368>") ### Do not delete this.
    await ctx.send("<:pogchamp:636572402054201368>")


@emoji.command(pass_context=True, name="pikachu", aliases=["pika", "pi"])
async def pikachu(ctx):
    # await ctx.send(f"{ctx.author.mention} says: <:pika:636581375612289024>") ### Do not delete this.
    await ctx.send("<:pika:636581375612289024>")


@emoji.command(pass_context=True, name="monkas", aliases=["m", "monkaS"])
async def monkas(ctx):
    # await ctx.send(f"{ctx.author.mention} says: <:monkas:645002369091764284>") ### Do not delete this.
    await ctx.send("<:monkas:636575202217689099>")


@bot.group(pass_context=True, name="meme", aliases=["m"])
async def meme(ctx):
    """Prints a specific meme."""
    if ctx.invoked_subcommand is None:
        await ctx.send("Please enter a valid meme. Valid memes: `typo`, `wig`.")
    else:
        return


@meme.command(pass_context=True, name="typo", aliases=["t"])
async def typo(ctx):
    """Sends the "TYPO! In the Groupchat" meme."""
    image = "assets/typo.jpg"
    await ctx.send(file=discord.File(image))


@meme.command(pass_context=True, name="wig", aliases=["w"])
async def wig(ctx):
    """Sends the "Wig" meme."""
    image = "assets/wig.jpg"
    await ctx.send(file=discord.File(image))


@meme.command(pass_context=True, name="wig2", aliases=["w2"])
async def wig2(ctx):
    """Y'all ready?"""
    video = "assets/wig.mp4"
    await ctx.send(file=discord.File(video))

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
        elif player_move == "rock" and bot_move == "paper":
            embed = discord.Embed(title=title, color=lose_color, description=f"I got Paper... {lose_desc}")
            await ctx.send(embed=embed)
        elif player_move == "rock" and bot_move == "scissors":
            embed = discord.Embed(title=title, color=win_color, description=f"I got Scissors... {win_desc}")
            await ctx.send(embed=embed)
        elif player_move == "paper" and bot_move == "rock":
            embed = discord.Embed(title=title, color=win_color, description=f"I got Rock... {win_desc}")
            await ctx.send(embed=embed)
        elif player_move == "paper" and bot_move == "paper":
            embed = discord.Embed(title=title, color=draw_color, description=f"I got Paper... {draw_desc}")
            await ctx.send(embed)
        elif player_move == "paper" and bot_move == "scissors":
            embed = discord.Embed(title=title, color=lose_color, description=f"I got Scissors... {lose_desc}")
            await ctx.send(embed)
        elif player_move == "scissors" and bot_move == "rock":
            embed = discord.Embed(title=title, color=lose_color, description=f"I got Rock... {lose_desc}")
            await ctx.send(embed)
        elif player_move == "scissors" and bot_move == "paper":
            embed = discord.Embed(title=title, color=win_color, description=f"I got Paper... {win_desc}")
            await ctx.send(embed)
        elif player_move == "scissors" and bot_move == "scissors":
            embed = discord.Embed(title=title, color=draw_color, description=f"I got Scissors... {draw_desc}")
            await ctx.send(embed)


@bot.command(pass_context=True, name="roll", aliases=["r"])
async def roll(ctx, *args):
    """Rolls dice. Format: `x`d`y`, ex. 2d6."""
    a = " ".join(args)
    s = ", "
    setup = re.fullmatch(r"(?P<howmany>[0-9]+)d(?P<howmuch>[0-9]+)", a)
    result = []
    hma = int(setup.group("howmany"))
    hmu = int(setup.group("howmuch"))
    if setup:
        if hma >= 100:
            await ctx.send("Do you... really need to roll so many dice..?")
            return
        elif hmu >= 100:
            await ctx.send("Do you... really need to roll dice with so many sides..?")
        elif hma == 0:
            await ctx.send("Please provide one or more dice to roll.")
            return
        elif hmu == 0:
            await ctx.send("Please provide the amount of sides you wish your dice to have.")
            return
        else:
            pass
        for x in range(hma):
            result.append(str(random.randint(1, hmu)))
        await ctx.send(f"{ctx.author.mention}: {hma}d{hmu} = {s.join(result)}.")
    else:
        await ctx.send("Please use a valid dice format. Example: `2d10`.")


@bot.command(pass_context=True, name="simpleroll", aliases=["sr"])
async def simpleroll(ctx, *, howmuch: int):
    """Simply chooses a random number between 1 and your input."""
    if howmuch >= 1000:
        await ctx.send(f"Do you... really need to generate such a high number..?")
        return
    else:
        for x in range(1):
            result = random.randint(1, howmuch)
            await ctx.send(f"{ctx.author.mention}: {result}.")


# Meta


@bot.command(pass_context=True, name="bug", aliases=["b"])
async def bug(ctx, bugname, *args):
    """Submits a bug to the dev."""
    channel = bot.get_channel(645409157217910794)
    await ctx.send("Alrighty! I'll make sure your report gets off to the dev right away!")
    await channel.send(f"Hey, boss! {ctx.author} wanted me to let you know about this!")
    embed = discord.Embed(title="Bug Report", color=discord.Color(0x6e0d25))
    embed.add_field(name=bugname, value=" ".join(args))
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await channel.send(embed=embed)


@bot.command(pass_context=True, name="suggestion", aliases=["suggest", "s"])
async def suggestion(ctx, suggestionname, *args):
    """Submits a suggestion to the dev."""
    channel = bot.get_channel(645409157217910794)
    await ctx.send("Alrighty! I'll make sure your suggestion gets off to the dev right away!")
    await channel.send(f"Hey, boss! {ctx.author} had an idea!")
    embed = discord.Embed(title="Suggestion", color=discord.Color(0x057a51))
    embed.add_field(name=suggestionname, value=" ".join(args))
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await channel.send(embed=embed)


# Owner Only


@bot.command(pass_context=True)
async def de(ctx, *args):
    """Echoes back what you say while deleting invocation for illusion of sentience."""
    cmd = ctx.message
    bad = ctx.message.author
    if ctx.author.id != 97153790897045504:
        await bad.send(f"You do not have permission to use that command! Context: `.de`.")
        await cmd.delete()
    else:
        await ctx.send(" ".join(args))
        await cmd.delete()


@bot.command(pass_context=True)
async def doomsday(ctx):
    """In case of the worst."""
    # I didn't want to have to use this.
    # blueflames = 510536932321656842
    cmd = ctx.message
    bad = ctx.message.author
    if ctx.author.id != 97153790897045504:
        await bad.send(f"You do not have permission to run that command! Context: `.doomsday`.")
        await cmd.delete()
    else:
        server = bot.get_guild(510536932321656842)
        await server.leave()


# Unfinished or For Testing


# On Message


@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    batty = 635484274023465000
    repeat = "__***FULLMETAL ALCHEMIST.***__\n"
    two = re.search(r"(2|two)!$", message.content.lower())
    if message.author.id != batty:
        out = ""
        if "fullmetal alchemist" in message.content.lower():
            out += repeat
        if "/shrug" in message.content:
            out += "¯\\_(ツ)_/¯\n"
        if message.content.startswith(".."):
            return
        if message.author.id == 461265486655520788 and message.channel.id != 414890945243512842:
            await message.delete()
        if two:
            image = "assets/2.gif"
            await ctx.send(file=discord.File(image))
        if out:
            await ctx.send(out)
        await bot.process_commands(message)


# TODO: Completed in current build:

# TODO: v1.2.+
# TODO: Challenge RPS


# TODO: Undefined
# TODO: Figure out how to store numbers that are linked to userid in a text doc or smth to recall at any time, cookies
# TODO: Challenge RPS
# TODO: Add Challenge RPS to help


# TODO: Long Way Off, hold 0 hope that these will ever happen
# TODO: Voice?


bot.run(TOKEN)
