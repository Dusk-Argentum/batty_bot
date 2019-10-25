# Changelog

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