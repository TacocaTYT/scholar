import disnake
from disnake.ext import commands

#------[COMMAND LINE ARGUMENT SETUP]------
import sys
import argparse
parser = argparse.ArgumentParser(description="A Discord Bot designed to assist Hexcasters in drawing or explaining patterns.")
parser.add_argument("-t", "--token", help="Supply a token for a bot account to connect under.", default="", type=str)
token = parser.parse_args()
if token == "": sys.exit("No Token, Cannot Connect")
#-----------------------------------------

client = commands.Bot(command_prefix="b|", test_guilds=[951923779859271711, 936370934292549712], intents=disnake.Intents.default())
client.pattern_index = []
client.gif_list = []
client.web_link = []

with open('patterns.txt', 'r') as file:
    for line in file:
        A, B, C = line.split('|')
        client.web_link.append(C)
        client.gif_list.append(B)
        client.pattern_index.append(A.strip())

@client.event
async def on_ready():
  print(f'Ready to Cast.')

@client.slash_command(
    name='pattern',
    description='Sends a gif of the pattern you enter, as found in the book.'
)
async def pattern(ctx, pattern : str):
    if pattern.casefold().replace("'", "").replace(":", "") in (pat.casefold().replace("'", "").replace(":", "") for pat in client.pattern_index):
        for i in range(len(client.pattern_index)):
            if pattern.casefold().replace("'", "").replace(":", "") == client.pattern_index[i].casefold().replace("'", "").replace(":", ""):
                assemble = disnake.Embed(color = disnake.Colour.purple(), title=client.pattern_index[i], url=f"https://gamma-delta.github.io/HexMod/#{client.web_link[i]}")
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
    assemble = disnake.Embed(color = disnake.Colour.purple(), title='Online Hexcasting Guide', url='https://gamma-delta.github.io/HexMod/')
    await ctx.send(embed=assemble)

@client.slash_command(
    name='topic',
    description='Sends a link to the online guidebook section for the given topic.'
)
async def guide(ctx, topic : str):
    assemble = disnake.Embed(color = disnake.Colour.purple(), title=f'Online Hexcasting Guide: {topic}', url=f'https://gamma-delta.github.io/HexMod/#patterns/{topic.lower().replace(" ", "_")}')
    await ctx.send(embed=assemble)
#token = input('bot token to connect under?\n')
client.run(token)
