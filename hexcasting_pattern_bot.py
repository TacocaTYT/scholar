import disnake
from disnake.ext import commands


client = commands.Bot(command_prefix="b|", test_guilds=[951923779859271711], intents=disnake.Intents.default())
client.pattern_index = []
client.gif_list = []

with open('patterns.txt', 'r') as file:
    pattern_catalogue = file.read()
    dummy = pattern_catalogue.replace('\n', '|').split('|')
    for i in range(len(dummy)):
        if i%2:
            client.gif_list.append(dummy[i])
        else:
            client.pattern_index.append(dummy[i])

@client.event
async def on_ready():
  print(f'Ready to Cast.')

@client.slash_command(
    name='pattern',
    description='Sends a gif of the pattern you enter, as found in the book.'
)
async def pattern(ctx, pattern : str):
    if pattern in client.pattern_index:
        for i in range(len(client.pattern_index)):
            if pattern == client.pattern_index[i]:
                await ctx.send(content=f'{client.gif_list[i]}')
    else:
        if pattern:
            await ctx.send(content=f'No pattern called {pattern}.', delete_after=5.0)
        else:
            await ctx.send(content='No pattern entered.', delete_after=5.0)

client.run('OTcxODMwNDIxNDU1MjY5OTE4.YnQNnA.o4lVGboEc-YBrARj8UDmjH0jzg4')