import requests
import asyncio

#SCRIPT BY LXGHTEND

#DM @Lxghtend ON DISCORD WITH QUESTIONS

#https://discord.com/api/v9/channels/845080693175222282/messages <---- gtp tc-sales

payload = {
    'content': "insert message" #<---- message that is sent
}

header = {
    'authorization': 'insert token' #<--- discord token
}

async def tc_sales_post_request():
    r = requests.post("https://discord.com/api/v9/channels/845080693175222282/messages", data=payload, headers=header) # change the discord api link to the channel u want link
    print("Message sent")
    await asyncio.sleep(1800)  #<---- change this number to change time between message (seconds)

while True:
    asyncio.run(tc_sales_post_request())
