# Changelog

## Batty Bot v1.3.6b

```diff
~ Apparently, neither Github nor Discord like when a + or - is preceeded by a tab. :pensive:
```

(Note: Why. Pushed on 6/13/20 @ 8:23 AM.)

## Batty Bot v1.3.6

```diff
+ Added some new things to the backend.
+ Added `asyncio` module.
- Removed some unused/testing/blank files from the file hierarchy.
~ Fixed `.bug` and `.suggestion` sending an error if no reaction is recieved within 60s.
~ Changed `.bug`'s embed color to better match the feel of a bug report. (Green > Red)
```

(Note: Smol update must mean big things are coming... Right..? :thinking: Also, changing changelog format again to better differentiate between additions, subtractions, and other changes by using `diff` syntax highlighting. Thank you, based Discord/Github, for having decent syntax highlighting. Pushed on 6/13/20 @ 8:19 AM.)

## Batty Bot v1.3.5

`~` Once again, overhauled `.help`.

	`~` Made the initial `.help` message more clean and organized.
	
	`~` Reordered certain categories to make all align to alphabetizing.
	
	`+` Added a line denoting that `Key Phrases` do not require the prefix to invoke.

`~` Made it so `.e pog`/`.e monkas` won't send their respective emoji twice.

`~` Changed `.bug`/`.suggestion` to use a more organized method of confirming/sending reports.

`~` Made it so anything that required triplequotes in the code no longer makes a whole new line/makes line formatting wonky.

`~` Backend changes:

	`+` Added `return` to the end of a lot of statements. (Please use `.bug` if anything is broken as a result of this.)
	
	`~` Changed around command/category orders in the code.
	
	`~` Renamed some internal `help` variables for cleanliness.
	
	`~` Various other extremely minor changes.
	
	`-` Removed some unnecessary lines.
	
(Note: Trying out a bit of a different approach to changelog logging, so changelogs might be a bit more thicc in the future. Pushed on 6/8/20 @ 9:12 EST.)

## Batty Bot 1.3.4

`~` Backend changes.

(Note: Working on some stuff. Just wanted to back up my work. Nothing to see here. Pushed on 6/4/20 @ 1:01 AM EST.)

## Batty Bot v1.3.3

`~` Changed BattyBot's icon! Happy Pride!

(Note: No major code changes, just wanted to draw attention to the new icon I made. Happy Pride! Stay safe! Pushed on 6/2/20 @ 2:02 PM EST.) 

## Batty Bot v1.3.2

`~` Changed some backend/developer commands to be more efficient, or work, depending on the case.

(Note: Some interesting stuff on the horizon. Keep an eye on this space! Pushed on 6/1/20 @ 5:35 PM EST.)

## Batty Bot v1.3.1

`+` Added welcome message for Snowlo.

`+` Added `.github`, which prints a message to Batty Bot's Github.

(Note: Just some extra things. Pushed on 5/11/20 @ 10:32 PM EST.)

## Batty Bot v1.3.0

`+` Added some additional aliases to some commands.

`+` Reinstated ToddBot suppression.

`~` Made absolutely sure that emotes from other users containing `pog` and `monkas` would not trigger Batty Bot's `:pogchamp:` or `:monkas:`. [Fixed this as per RFC#001.]

`~` Some developer-only commands were overhauled.

(Note: A bit of a smaller version-up update, mostly because I couldn't think of anything else new to add. Please remember that the `.suggestion` command exists, so I can get new ideas! Pushed on 4/23/20 @ 12:57 AM EST.)

## Batty Bot v1.2.10

`+` Added `turnipchamps` to `.role` for consistency.

`-` Removed ToddBot suppression.

`~` Other backend changes.

(Note: Nothing here. Pushed on 4/24/20 @ 10:36 PM EST.)

## Batty Bot v1.2.9

`~` Fixed issue wherein using an emote containing `pog` or `monkas` would call up the `pogchamp` and `monkas` emojis redundantly.

(Note: I should have fixed this months ago. Pushed on 4/22/20 @ 10:14 PM EST.)

## Batty Bot v1.2.8

`~` TOTALLY overhauled `.roll`. Check it out! It can add the result of multiple numbers now. This took me months to figure out. Please clap.

`~` Other minor changes throughout program.

(Note: Happy 6 month anniversary! Pushed on 4/21/20 @ 10:27 PM EST.)

## Batty Bot v1.2.7

`+` Added `.m chime`, which sends the "Oh? You're a chime?" meme.

`+` Added `.m chime` to `.help`.

`~` Fixed `.rps`, which threw an unhelpful error due to some absentminded programming on my part.

`~` Changed `.help` to accurately reflect the change to my Discord tag.

(Note: `.m chime` requested by Jakpatch#5840. I can't believe it took me months to fix the `.rps` error... To be fair, I didn't know about it until today, and fixed it immediately. Also, just noticed the past few changelogs don't have AM or PM to denote what times they were pushed. Whoops. Pushed on 4/13/20 @ 8:26 AM EST.)

## Batty Bot v1.2.6

`+` Added the `Turnipchamps` role react! Now, simply react to the message in <#636366607626666014> with the turnip emoji to be notified when peoples' turnip prices are looking good.

(Note: This should be good for all of our amazing ACNH players on the server. Pushed on 4/06/20 @ 2:52 EST.)

## Batty Bot v1.2.5

`+`/`-`/`~` Added, removed, and changed various things.

(Note: Just some miscellaneous small changes over the course of the past 3 months that weren't committed. Pushed on 3/12/20 @ 8:04 EDT.)

## Batty Bot v1.2.4

`+` Added the ability to print the `monkas` and `pogchamp` emojis by simply saying `monkas` or `pog`/`pogchamp`, without the need for the command.

`+` Added `wig2` to `.meme`'s error message. Did this a LONG time ago, just didn't feel like making a changelog entry just for it.

`+` Added `.purge`, a command only usable by the bot's creator (hehe, that's me!) to delete a bunch of the bot's messages, in case something goes wrong and a lot need to be deleted at once.

(Note: Just a small update for now. I'm working on some bigger stuff, but will be pushing that later. Sorry about nothing for a month! Hoping to get the bigger one out before the end of the year. Pushed on 12/22/19 @ 8:56 PM EDT.)

## Batty Bot v1.2.3

`+` Added `wig2`, a new argument to `.meme`, which sends a video clip of two people saying "wig" to each other, and added this to `.help`/`.help meme`.

(Note: Wig. Wig. I'm ready. Pushed on 11/21/19 @ 2:58 PM EDT.)

## Batty Bot v1.2.2

`+` Added `-pm` argument to `.help`. I had it commented out before, but forgot to add it. Whoops.

`!` Fixed critical error in Reaction Role and `.role`, caused by Discord updating its API in the middle of the night without warning.

(Note: Discord boutta catch some hands over this. Pushed on 11/19/19 @ 11:09 AM EDT.)

## Batty Bot v1.2.1

`~` Fixed `.e monkas`. It wasn't working for a bit there monkaS

`~` Made some adjustments to the way the bot responds to prompts that are in `on_message`, like `2!` and `Fullmetal Alchemist`. Everything should work now.

`~` Changed the `.help` a bit, and added `2!` to it.

(Notes: Just some small bugfixes this time around. Please don't hesitate to use `.b "bug name" [description]` if you ever find a bug! Pushed on 11/18/19 @ 6:45 PM EDT.)

## Batty Bot v1.2!.0

`+` Added `.bug`, which allows you to submit bug reports directly to me.

`+` Added `.suggestion`, which allows you to submit suggestions directly to me.

`+` Added `.meme`, which is now what `.typo` and `.wig` are.

`+` Added `monkaS` to `.emoji`, for those tense moments.

`+` Added `.help` for every single command, which goes into more detail about aliases and invocation on every command.

`+` Added `-pm` argument to every help, which PMs the help to you, instead of posting it in the channel.

`-` Removed previously mentioned compatability with another server.

`-` *Technically* removed `.typo` and `.wig`, but they're in `.meme` now, so it's OK.

`~` Renamed `.rockpaperscissors` to `.rps`. Who the hell is gonna type `.rockpaperscissors`?

`~` Made `.rps`'s output look prettier, I think.

`~` TOTALLY overhauled `.help`. Formatting changes and the like.

`~` Added a maximum to `.simpleroll`. Too big numbers hurts my computer.

`~` Added a maximum for `howmuch` on `.roll`. No more rolling 1d200000, Gage.

`~` Changed the backend of how `fullmetal alchemist` works. Now, ANY case works.

`~` Reorganized the role names in `.role`'s "no arguments" error. They were out of alphabetical order.

`~` Organized file structure a bit more.

(Notes: There's a bit more in the works, yet, so stay tuned! Pushed on 11/16/19 @ 8:55 EDT.)

## Batty Bot v1.1.0

`+` Added `.eightball`, which gives a very vague and cryptic answer to any questions you may have.

`+` Added `.rockpaperscissors`, a fun little game you can play with the bot.

`+` Added `.roll`, which rolls `x`d`y` and outputs the result(s). There's a maximum, I won't say, but it exists.

`+` Added `.simpleroll`, which simply rolls between 1 and whichever number you input.

`+` Added (tenative) compatability with another server. They begged. Blame Phylus.

`+` Added `/shrug` to `.help`. Was added in an earlier build, forgot to add to `.help`.

`+` Added a thumbnail to `.help`, just to make it look prettier. :)

`+` Added `TODO` section to the code. If you're looking for what's happening in the future, keep an eye on that space.

`~` Reorganized `.help`, everything should be in alphabetical order now. Should be.

`~` Changed some words in `.help`.

`~` Changed the footer of `.help` to be... I think a bit more clear?

`~` Reorganized the code, everything is in an order that makes sense now, mostly.

`~` The code is now PEP-8 compliant! Now my IDE will stop putting so many fucking colors in the scroll bar.

`-` Removed `.dotdot`. It was added to catch `...`, `..!`, `..?`, etc., but I ended up with a redundancy from something that made more sense in the `on_message` event.

(Notes: At long last, here's Batty Bot v1.1.0. I worked many hard on this, listened to many music compilations, consulted for much advice [shoutout to the lads over on AvraeDev!], and ate many pretzels. This's been a couple of days in the making, and I'm planning on adding so much more and continuing work on this project. Thank you very much for continuing to use the bot! Every time someone uses a command, literally, every single time, I feel a bit more proud of myself for managing to cobble this all together. I look forward to your continued use and support! Pushed on 11/3/19 @ 2:57 EDT.)

## Batty Bot v1.0.11

`+` Added `.typo`, which sends the "TYPO! In the groupchat" meme.

(Notes: Hats are not mv0, even in windy conditions. You can't change my mind. Pushed on 11/1/19 @ 1:56 PM.)

## Batty Bot v1.0.10

`+` Added an official of declaration of war against known committer of crimes against humanity, Todd Bot. Batty Bot will automatically delete any messages from Todd Bot to protect you and yours from Todd Bot's sweet little lies.

`+` Added `/shrug`, which invokes the Shrug [kaomoji](http://kaomoji.ru/en/), different from Discord's builtin, which has to be at the beginning, this can be anywhere.

`+` Added more helpful error text for `.emoji`.

`~` Changed the ellipsis handling to instead catch on `..` (compared to `...`), to handle expressions like `..?` and `..!`.

(Notes: Happy Halloween! The version numbers will keep ticking up in the third place until a major update, think like Minecraft's version numbers. Pushed on 10/31/19 @ 4:36 PM EST.)

## Batty Bot v1.0.9

`+` Added `.wig` to `.help`.

`+` Added a single word to `.emoji` help as a shorthanded way to get fields to interact properly.

`+` Added a new invocation to Fullmetal Alchemist (henceforth referred to as "FMA").

`~` Changed FMA's section of `.help` to not be as long, I think.

`~` Changed the "Emojis" section of `.help` to "Fun", so I don't have to add any more fields.

`~` Changed the way the FMA thing works again, so I don't have to type the bot's id every time, nor the actual FMA text.

(Notes: I can't believe I forgot to add something to the `.help`. Again. Pushed on 10/26/19 @ 5:35 PM EST.)

## Batty Bot v1.0.8

`+` Added `.wig`, by request of Chem#8601. Uploads the meme.

`+` Added full ellipsis error handling. Ellipsis lovers, unite...!

`~` Changed some `pass`es to `return`s.

`-` Removed an unnecessary `print` function. I don't really *need* to know every time someone uses an ellipsis and we avoid disaster.

(Notes: Thanks, Naric, for the idea for `.wig`, and for revealing the "critical" [/s] vulnerability with the way I handled ellipses. Are you tired of reading the words "ellipses" and "ellipsis" yet? Pushed on 10/26/19 @ 5:23 PM EST.)

## Batty Bot v1.0.7b

`+` Added(?) `...`. It does nothing, but it prevents the bot from yelling at people who say `...`.

(Notes: An ingenious fix for the problem of... uh... ellipses.)

## Batty Bot v1.0.7
`+` Added error handling. The bot might just plain yell at you if you start a sentence with `.`, ever. I will have to work on that.

`-` Removed some comments that I didn't need anymore.

`?` Screwed with Fullmetal Alchemist code, it shouldn't be broken, but I think it's a bit different.

(Notes: The error handling issue brings up an interesting question, if I should keep the prefix as `.`, because if you start ANY message with a `.` it will now yell that you're not using a real command. It'll yell at people for sending `...`, or any variant, as well. Might experiment with other prefixes, idk. Pushed on 10/25/19 @ 3:14 PM EST.)

## Batty Bot v1.0.6
`+` Added "Key Phrases" section to `.help`, so that `fullmetal alchemist` and co.'s existence is documented *somewhere*.

`~` Added an error handler to `.de` now that it's public knowledge. Only **I** get to pretend the bot's sentient >:(

`~` Changed the invokation context for `fullmetal alchemist` and co., so that it triggers whenever the phrase is any where in any message, as opposed to the message starting with it.

(Notes: So soon after the last one, just some housekeeping and a tweak. Pushed on 10/24/19 @ 9:37 PM EST.)

## Batty Bot v1.0.5
`+` Added the ability to echo "__***`FULLMETAL ALCHEMIST`***__" when anyone says "fullmetal alchemist"/"Fullmetal Alchemist"/"FULLMETAL ALCHEMIST", based off of that one tumblr post where the person wanted to add this self-same feature but forgot to make an exit condition.

(Notes: This was just for fun. I'm running out of ideas. Please help. Pushed on 10/24/19 @ 9:05 PM EST.)

## Batty Bot v1.0.4
`+` Added `.emoji`, which lets a user use specific external emojis! Currently supported: `pogchamp`, `pikachu`.

`+` Added `.emoji` and its subcommands to `.help`.

`~` Fixed `.role` help sending both the Role command help and the basic help.

`~` Made `.help` a bit more clear about command syntax for `.role` (and `.emoji`).

(Notes to users: I actually have the line of code that prints the name of the person who invokes .emoji already written, it's just commented out because it makes the emoji itself look smaller. Do not abuse the fact that the bot currently does not mention the user in order to spam, or you will have prettier-looking emojis taken away from everyone. General notes: Pushed on 10/23/19 @ 11:16 AM.)

## Batty Bot v1.0.3
`+` Added sentience capabilities, apparently?

(Notes: This added the owner-only `.e` command, which echoes a message while removing the invoking message, to make it look like the bot sent the message of it's own accord. Pushed on 10/22/19 @ 11:41 PM EST.)

## Batty Bot v1.0.2
`~` Changed the .role commands to a different text syntax for naming the role after granting it to you, to match the new (read: fixed) Greetings message syntax.

`~` Changed the message sent to users after they sign up for roles via reactions to match the selfsame syntax previously mentioned for consistency's sake.

(Notes: Pushed on 10/22/19 @ 11:00 PM EST.)

## Batty Bot v1.0.1
`+` Implemented Batty Bot!

`+` Added `.test`, `.help`, and `.role` commands.

`+` Added ability to grant Greetings, Gamers, and Socialists through reactions in #role-call.

`+` Added ability to grant roles via `.role`.

`+` Added ability to greet new users when they join.

`~` Fixed greeting new users.

(Notes: Skipped 1.0.0, due to the Greetings message being broken, fixed basically immediately in v1.0.1. Pushed on 10/22/19 @ 10:42 PM EST.)