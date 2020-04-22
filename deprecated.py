# These are just things I needed to store some place, didn't feel like deleting them, but their comments would have drove me nuts.

# @bot.command(pass_context=True, name="roll3", aliases=["r3"])
# async def roll3(ctx, *args):
    # a = " ".join(args)
    # setup = re.fullmatch(r"(?P<howmany>[0-9]+)d(?P<howmuch>[0-9]+)", a)
    # hma = int(setup.group("howmany"))
    # hmu = int(setup.group("howmuch"))
    # if setup:
        # for x in range(hma):
            # roll = random.randint(1, hmu)
            # await ctx.send(f"{ctx.author.mention}: {hma}d{hmu} = {roll}.")
    # else:
        # await ctx.send("Please use a valid dice format. Example: `2d10`.")
		

# @bot.event
# async def on_member_join(ctx):  # Welcomes a new user when they join.
    # welcome_channel = bot.get_channel(290304276381564928)
    # await welcome_channel.send(f"<@&636374013731667969>, {ctx.mention}! Welcome to Gazia's Bat Den! Please read <#413876271865528320>, and enjoy your stay!")

# @bot.event
# async def on_message(message):
    # ctx = await bot.get_context(message)
    # batty = 635484274023465000
    # repeat = "__***FULLMETAL ALCHEMIST.***__"
    # two = re.search(r"2!$", message.content)
    # two = re.search(r"(2|two)!$", message.content.lower())
    # if "fullmetal alchemist" in message.content.lower() and message.author.id != batty:
        # await ctx.send(repeat)
    # elif "/shrug" in message.content and message.author.id != batty:
        # await ctx.send("¯\\_(ツ)_/¯")
    # elif message.content.startswith("..") and message.author.id != batty:
        # return
    # elif message.author.id == 461265486655520788 and message.channel.id != 414890945243512842:
        # await message.delete()
    # if two and message.author.id != batty:
        # image = "assets/2.gif"
        # await ctx.send(file=discord.File(image))
    # await bot.process_commands(message)


# @bot.command(pass_context=True, name="roll", aliases=["r"])
# async def roll(ctx, *args):
    # """Rolls dice. Format: `x`d`y`, ex. 2d6."""
    # a = " ".join(args)
    # s = ", "
    # setup = re.fullmatch(r"(?P<howmany>[0-9]+)d(?P<howmuch>[0-9]+)", a)
    # result = []
    # hma = int(setup.group("howmany"))
    # hmu = int(setup.group("howmuch"))
    # if setup:
        # if hma >= 100:
            # await ctx.send("Do you... really need to roll so many dice..?")
            # return
        # elif hmu >= 100:
            # await ctx.send("Do you... really need to roll dice with so many sides..?")
            # return
        # elif hma == 0:
            # await ctx.send("Please provide one or more dice to roll.")
            # return
        # elif hmu == 0:
            # await ctx.send("Please provide the amount of sides you wish your dice to have.")
            # return
        # else:
            # pass
        # for x in range(hma):
            # result.append(str(random.randint(1, hmu)))
        # await ctx.send(f"{ctx.author.mention}: {hma}d{hmu} = {s.join(result)}.")
    # else:
        # await ctx.send("Please use a valid dice format. Example: `2d10`.")