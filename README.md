# CeaseBot
Discord bot for messing with your users
Author: Vlad Pelin

---

Discord bot made using DiscordPy (https://github.com/Rapptz/discord.py).

Though simple, this bot's purpose is primarily to mess with the members of a server. At the moment, I've customised it to work on the FH Knights Discord server, to mess with the members who post NSFW content or spammers. It makes use of a list of "bad words", which it looks for and, depending on its mood, responds in a certain way. The bot also has special cases for some members if they attempt to talk to it.

Stuff left to implement:
  - add reactions to comments (at the moment, passing it an emoji causes an HTTP bad request error)
  - embed links/photos/videos (fix permisions first)
  - more special cases for users
  - more user interaction
  
-----

CHANGELOG:

v0.1
  - first release
  - minimal user interaction
  - moods
  - timer on "bad word" occurence, so it doesn't spam
