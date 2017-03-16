import discord
import asyncio
import logging
import random
import time
from discord.ext.commands import Bot
from discord import Game
from discord import Emoji
import os
import psutil

##bot invite link: https://discordapp.com/oauth2/authorize?client_id=291290722135572483&scope=bot&permissions=19520
##currently, the bot is hosted locally, so it's only online if it's running on local machine

logging.basicConfig(level=logging.INFO)

ceasebot = Bot(command_prefix="!")

bad_words = ['furry', 'furrie', 'scalie', 'snek', 'trap', 'gay', 'ledgie', 'anime', 'animu']
states = {15: 'Not-so-calm', 30: 'Angry', 45: 'Jimmies Rustled', 70: 'Mad', 90: 'Very Mad', 120: 'NUKING CHAT'}
deusbot_commands=['!bodypillow', '!cease', '!edgy', '!end', '!heresy', '!heretic', '!traps', '!weeb', '!wtf', '!kys', '!exterminatus', '!baddog', '!bash', '!ledge']
current_state = 'Calm'
bad_word_count = 0
start_time_spam = 0
elapsed_time_spam = 0
start_time = 0
elapsed_time = 0
ree = False

process = psutil.Process(os.getpid())
print(process.memory_full_info().uss)

@ceasebot.event
async def on_message(message):

    global current_state
    global bad_word_count
    global ree
    global checked_words
    global start_time_spam
    global elapsed_time_spam
    global start_time
    global elapsed_time
    global deusbot_commands

    elapsed_time = int(time.monotonic())

    if int(elapsed_time - start_time) > 30:
        for word in bad_words:
            if word in message.content.lower():
                if current_state == 'Calm':
                    await ceasebot.send_message(message.channel, 'Please, stop talking about that.')
                    start_time = int(time.monotonic())
                    bad_word_count += 1
                    break
                elif current_state == 'Not-so-calm':
                    await ceasebot.send_message(message.channel, 'I said *please*. I won\'t be so nice if you keep discussing stuff like this')
                    start_time = int(time.monotonic())
                    bad_word_count += 1
                    break
                elif current_state == 'Angry':
                    await ceasebot.send_message(message.channel, 'I said fucking **stop**. This is low-tier shitposting. I hate this.')
                    start_time = int(time.monotonic())
                    bad_word_count += 1
                    break
                elif current_state == 'Jimmies Rustled':
                    await ceasebot.send_message(message.channel, 'Fucking hell, why would you keep posting about stuff like that. Stop. **Stop**. Christ.')
                    start_time = int(time.monotonic())
                    bad_word_count += 1
                    break
                elif current_state == 'Mad':
                    await ceasebot.send_message(message.channel, 'Jesus fucking Christ, no more. ***Stop this at once***')
                    start_time = int(time.monotonic())
                    bad_word_count += 1
                    break
                elif current_state == 'Very Mad':
                    await ceasebot.send_message(message.channel, '***STOP, JUST PLEASE FUCKING STOP THIS SHIT. CEASE***')
                    start_time = int(time.monotonic())
                    bad_word_count += 1
                    break
                elif current_state == 'NUKING CHAT':
                    if not ree:
                        await ceasebot.send_message(message.channel, '***MORE? YOU\'VE DONE IT NOW***')
                        bad_word_count += 1
                        start_time_spam = int(time.monotonic())
                        elapsed_time_spam = int(time.monotonic())
                        ree = True
                    if elapsed_time_spam - start_time_spam < 10:
                        for i in range(4):
                            await ceasebot.send_message(message.channel, random.choice(deusbot_commands))
                        elapsed_time_spam = int(time.monotonic())
                    else:
                        await ceasebot.send_message(message.channel, 'Lewd content has been purged from this chat. I\'m **calm** again.')
                        current_state = 'Calm'
                        bad_word_count = 0
                    start_time = int(time.monotonic())
                    break
                
    if ('apolly' in message.author.display_name.lower() and 'ceasebot' in message.content.lower()):
        await ceasebot.send_message(message.channel, '{} Yes, Mother?'.format(message.author.mention))
        await ceasebot.wait_for_message(author=message.author, content='Howl')
        await ceasebot.send_message(message.channel, '***AWOOOOOOO***')
        
    if ('edge' in message.author.name.lower() and 'ceasebot' in message.content.lower()):
        await ceasebot.send_message(message.channel, '{} Yes, Edgy?'.format(message.author.mention))
        msg = await ceasebot.wait_for_message(author=message.author)
        if 'lmao' in msg.content.lower():
            await ceasebot.send_message(message.channel, '{} ayyy lmao'.format(message.author.mention)) 
        
    if ('apfelin' in message.author.name.lower() and 'ceasebot' in message.content.lower()):
        await ceasebot.send_message(message.channel, '{} Yes, Master?'.format(message.author.mention))
        msg = await ceasebot.wait_for_message(author=message.author)
        if 'how are you?' in msg.content.lower():
            await ceasebot.send_message(message.channel, 'Fine.')
        elif 'what do you think of' in msg.content.lower()
            await ceasebot.send_message(message.channel, '{} He\'s dumb.'.format(message.author.mention))
        
    if bad_word_count in states:
        current_state = states[bad_word_count]

ceasebot.run('MjkxMjkwNzIyMTM1NTcyNDgz.C6ndNQ.KUgdX7U_rb7NPMJS7R_OChidhTE')
