from cgitb import html
from urllib import request, response, error, parse
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import discord


TOKEN = 'ODUzNzA0NzQ4NTU3NTMzMjY1.YMZQgQ.KJvP-F8G3SPRIwHSU38ufxF8Yt0'

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is online")

@client.event
async def on_message(message):
    
    exclamation_mark = '!'
    if message.author == client.user:
        return
    if exclamation_mark  in message.content:

        user_msg = message.content
        print("MESSAGE IS: " + user_msg)
        print(user_msg.replace('!',''))
        #user_msg.replace('!','')

        URL = (f"https://na.op.gg/summoners/na/{user_msg.replace(' ','%20')}")
        hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        req = Request(URL,headers=hdr)
        html = request.urlopen(req)
        soup = BeautifulSoup(html, "html.parser")

        ranked_solo = soup.find("div", {"class": "type"}).text

        try:
            tier_rank =  soup.find("div", {"class": "tier-rank"}).text
        except:
            print("No rank found")
            await message.channel.send("User is unranked")
        LP = soup.find("span",{"class":"lp"}).text
        win_lose = soup.find("span",{"class":"win-lose"}).text

        print(ranked_solo)
        print(tier_rank)
        print(LP)
        print(win_lose)

        await message.channel.send(f"{user_msg.replace('!','')} is {tier_rank} with {LP}. \nStats: {win_lose} \nhttps://na.op.gg/summoners/na/{user_msg.replace(' ','%20')}")

client.run(TOKEN)


