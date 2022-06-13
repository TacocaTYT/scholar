import disnake
from disnake.ext import commands


client = commands.Bot(command_prefix="b|", test_guilds=[951923779859271711, 936370934292549712], intents=disnake.Intents.default())
client.pattern_index = []
client.gif_list = []
client.web_link = []

with open('patterns.txt', 'r') as file:
    pattern_catalogue = file.read()
    dummy = pattern_catalogue.replace('\n', '|').split('|')
    for i in range(len(dummy)):
        if i%3 == 2:
            client.web_link.append(dummy[i])
        elif i%3 == 1:
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
                assemble = disnake.Embed(color = disnake.Colour.purple(), title=client.pattern_index[i], url=client.web_link[i])
                assemble.set_image(url=client.gif_list[i])
                await ctx.send(embed=assemble)
    else:
        if pattern:
            await ctx.send(content=f'No pattern called {pattern}.', delete_after=5.0)
        else:
            await ctx.send(content='No pattern entered.', delete_after=5.0)

@client.slash_command(
    name='guide',
    description='Sends a link to the online guidebook, courtesy of Alwinfy.'
)
async def guide(ctx):
    assemble = disnake.Embed(color = disnake.Colour.purple(), title='Online Hexcasting Guide', url='https://bl.ocks.org/Alwinfy/raw/455d2d4af12bd893b46170056ca1714f/')
    await ctx.send(embed=assemble)

@client.slash_command(
    name='constants',
    description='Sends a link to the section on numerical constants in the online book.'
)
async def guide(ctx):
    assemble = disnake.Embed(color = disnake.Colour.purple(), title='Numerical Constants', url='https://bl.ocks.org/Alwinfy/raw/455d2d4af12bd893b46170056ca1714f/#patterns/consts')
    await ctx.send(embed=assemble)


client.run('OTcxODMwNDIxNDU1MjY5OTE4.YnQNnA.o4lVGboEc-YBrARj8UDmjH0jzg4')