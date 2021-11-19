import requests
import re
from pycoingecko import CoinGeckoAPI
import discord
from discord.ext.commands import Bot

cg = CoinGeckoAPI()

bot = Bot(command_prefix='!')
TOKEN = 'TOKEN'

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.command()
async def crypto(ctx, message=None):
    if message == 'btc' or message == 'BTC':
        message = 'bitcoin'
    elif message == 'eth' or message == 'ETH':
        message = 'ethereum'
    if cg.get_price(ids=message, vs_currencies='usd') != {}:
        coin = str(cg.get_price(ids=message, vs_currencies='usd'))
        value = float(re.sub("[^0-9^.]", "", coin))
        formatted = "{:,.2f}".format(value)
        embed = discord.Embed(title='The price of ' + message.capitalize() + ' is: ', description=  '$' +formatted, color=0x058a33)
        await ctx.send(embed=embed)
    else:
        await ctx.send('Invalid token. Only btc and eth are valid shorthands.')



bot.run('TOKEN')

