import discord 
from discord import app_commands
from discord.ext import commands

TOKEN = "" # Paste your bot token between these Quotation marks.

client = commands.Bot(command_prefix='?', intents= discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    print('OK')
    try:
        synced = await client.tree.sync()
        print(f'synced {len(synced)} command(s)')
    except Exception as e:
        print(e)



@client.tree.command(name='hello') # Output: Hello!. 
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message('Hello!')
    ephemeral = True

@client.tree.command(name='hello2') # Output: @YOURNAME Hello!
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'{interaction.user.mention} Hello!')
    ephemeral = True




client.run(TOKEN) # Do Not Touch.
