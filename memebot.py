import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme') ## requests helps make http req to urls
  json_data = json.loads(response.text) ## read json data
  return json_data['url']

class MyClient(discord.Client): ## this class myclient is interacting the the discord api
## it's created by extending discord.client
    async def on_ready(self): ## onready called when login is successful
        print('Logged on as {0}!'.format(self.user))

    ## read and respond to messages
    async def on_message(self, message): ## onmessage gets called automatically anytime
    ## there's a new message BUT
        if message.author == self.user: ## first check if the bot is sending messages
            return ## don't text yourself

        if message.content.startswith('$meme'): ## respond to speacial keyword
            await message.channel.send(get_meme())

## intents for a given instance of myclient
intents = discord.Intents.default() ## since it's default it has to be explicitly
## stated that it can interact with messages
intents.message_content = True ## through this

client = MyClient(intents=intents) ## instantiate myclient then run
client.run("*********")