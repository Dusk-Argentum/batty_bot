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
    elif ctx.guild.id == 510536932321656842:
        welcome_channel = bot.get_channel(510536932325851137)
        image = "rielle.gif"
        await welcome_channel.send(f"Welcome, {ctx.mention}! Please enjoy your stay.")
        await welcome_channel.send(file=discord.File(image))
    elif ctx.guild.id == 348897377400258560:
        welcome_channel = bot.get_channel(348897378062827520)
        await welcome_channel.send("what")


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


# General


@bot.group(pass_context=True, name="help2", aliases=["cmds", "commands", "h", "h-hewp!!!", "help"])
async def help2(ctx):
    """The help command."""
    if ctx.invoked_subcommand is None:
        embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
        embed.add_field(name="General", value="""`.help` \n Shows this help. \n `.test` 
        Sends a test message to check if the bot's online.""", inline=True)
        embed.add_field(name="Roles", value="""`.role [subcommand]` 
        Assign yourself a specific role via command.""", inline=True)
        embed.add_field(name="Fun", value="""`.eightball`
        Gives a cryptic answer to your queries. \n `.emoji [subcommand]`
        Have the bot print out a very specific emoji. \n `.rockpaperscissors`
        Play Rock, Paper, Scissors with the bot. \n `.roll` \n Rolls dice. Format: `x`d`y`, ex. 2d6.
        `.simpleroll` \n Simply chooses a random number between 1 and your input. \n `.typo`
        Sends the "TYPO! In the Groupchat" meme. \n `.wig` \n Sends the "wig" meme.""", inline=True)
        embed.add_field(name="Key Phrases", value="""`Fullmetal Alchemist`
        Causes the bot to repeat the phrase, but louder.
        `/shrug` \n Prints "¯\\_(ツ)_/¯", no matter where `/shrug` is in your message.""", inline=True)
        embed.set_footer(text="""If a command has subcommands,
        do `.help [command name]` for further help. Made by Dusk-Argentum#6530!""")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
        await ctx.send(embed=embed)
    else:
        return


@help2.command(pass_context=True)
async def role(ctx):
    """Help for `.role`."""
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
    embed.add_field(name="`.role` [Subcommands]", value="""`greetings` \n Adds or removes the Greetings role from you.
    `gamers` \n Adds or removes the Gamers role from you. \n `socialists`
    Adds or removes the Socialists role from you.""", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.send(embed=embed)


@help2.command(pass_context=True)
async def emoji(ctx):
    """Help for `.emoji`."""
    embed = discord.Embed(title="Batty Bot's Commands!", color=discord.Color(0xE8B52A))
    embed.add_field(name="`.emoji` [Subcommands]", value="""`pogchamp` \n Sends Pogchamp.
    `pikachu` \n Sends Surprised Poketch-chu.""", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/348897378062827520/640434972720758784/bat.jpg")
    await ctx.send(embed=embed)


@bot.command(pass_context=True, name="test", hidden=True)  # Basically, confirm that the bot is still online.
async def test(ctx):
    """ Confirms whether or not the bot is online, basically. """
    await ctx.send("I work!")


# Role


@bot.group(pass_context=True, name="role")
async def role(ctx):
    """Adds or removes a role."""
    if ctx.invoked_subcommand is None:
        await ctx.send("Please choose a role. Valid roles: `Greetings`, `Gamers`, and `Socialists`.")


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


@bot.command(pass_context=True, name="eightball", aliases=["8", "8ball"])
async def eightball(ctx):
    """Gives a cryptic answer to your queries."""
    answer = random.choice(["Yes.", "No.", "Possibly.", "Not likely.", "It's up to you.", "It's out of your control.",
                            "I can't say.", "That is beyond the scope of my programming."])
    await ctx.send(answer)


@bot.group(pass_context=True, name="emoji", aliases=["e", "emote"])
async def emoji(ctx):
    """Have the bot print out a very specific emoji."""
    if ctx.invoked_subcommand is None:
        await ctx.send("Please enter a valid emoji. Valid emojis: `pogchamp`, `pikachu`.")
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


@bot.command(pass_context=True, name="rockpaperscissors", aliases=["rps"])
async def rockpaperscissors(ctx, move):
    """Play Rock, Paper, Scissors with the bot."""
    player_move = move.lower()
    bot_move = random.choice(["rock", "paper", "scissors"])
    if player_move not in "rock paper scissors":
        await ctx.send("Invalid move! Valid moves: ... you should know.")
    else:
        if player_move == "rock" and bot_move == "rock":
            await ctx.send(f"I got Rock... We drew, {ctx.author.mention}.")
        elif player_move == "rock" and bot_move == "paper":
            await ctx.send(f"I got Paper... I win!")
        elif player_move == "rock" and bot_move == "scissors":
            await ctx.send(f"I got Scissors... You win, {ctx.author.mention}!")
        elif player_move == "paper" and bot_move == "rock":
            await ctx.send(f"I got Rock... You win, {ctx.author.mention}!")
        elif player_move == "paper" and bot_move == "paper":
            await ctx.send(f"I got Paper... We drew, {ctx.author.mention}.")
        elif player_move == "paper" and bot_move == "scissors":
            await ctx.send(f"I got Paper... I win!")
        elif player_move == "scissors" and bot_move == "rock":
            await ctx.send(f"I got Rock... I win!")
        elif player_move == "scissors" and bot_move == "paper":
            await ctx.send(f"I got Paper... You win, {ctx.author.mention}!")
        elif player_move == "scissors" and bot_move == "scissors":
            await ctx.send(f"I got Scissors... We drew, {ctx.author.mention}.")


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
    for x in range(1):
        result = random.randint(1, howmuch)
        await ctx.send(f"{ctx.author.mention}: {result}.")


@bot.command(pass_context=True, name="typo")
async def typo(ctx):
    """Sends the "TYPO! In the Groupchat" meme."""
    image = "typo.jpg"
    await ctx.send(file=discord.File(image))


@bot.command(pass_context=True, name="wig", aliases=["w"])
async def wig(ctx):
    """Sends the "Wig" meme."""
    image = "wig.jpg"
    await ctx.send(file=discord.File(image))


# Owner Only


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


# On Message


@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    batty = 635484274023465000
    repeat = "__***FULLMETAL ALCHEMIST.***__"
    if "fullmetal alchemist" in message.content and ctx.author.id != batty:
        await ctx.send(repeat)
    elif "Fullmetal Alchemist" in message.content and ctx.author.id != batty:
        await ctx.send(repeat)
    elif "FULLMETAL ALCHEMIST" in message.content and ctx.author.id != batty:
        await ctx.send(repeat)
    elif "Fullmetal alchemist" in message.content and ctx.author.id != batty:
        await ctx.send(repeat)
    elif "/shrug" in message.content and ctx.author.id != batty:
        await ctx.send("¯\\_(ツ)_/¯")
    elif message.content.startswith("..") and ctx.author.id != batty:
        return
    elif message.author.id == 461265486655520788 and message.channel.id != 414890945243512842:
        await message.delete()
    await bot.process_commands(message)


# TODO: v1.1+
# TODO: Embeds on RPS, others
# TODO: Redo fma to consider lower
# TODO: Suggestion submission command


# TODO: Undefined
# TODO: Figure out how to store numbers that are linked to userid in a text doc or smth to recall at any time, cookies
# TODO: Absorb 2!'s powers.


# TODO: Long Way Off, hold 0 hope that these will ever happen
# TODO: Voice?


# Done in 1.1: Roll, simpleroll, rps, 8ball, redo help, blueflames compat, shrug to help, added thumbnail to help
# Removed dotdot, pep8 compat, reorganized code


bot.run(TOKEN)
