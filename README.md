# Changelog

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