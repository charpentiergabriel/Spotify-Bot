import discord
from discord import Spotify
from discord.ext import commands

intents = discord.Intents().all()
client = discord.Client(intents = intents)

#async def delete_channel(ctx, channel_name):
#   existing_channel = discord.utils.get(client.guilds[0].channels, name=channel_name)
#   await existing_channel.delete()

@client.event
async def on_member_update(before, after):
    member = after
    cats = client.guilds[0].categories
    for c in cats:
        if c.name == 'artists':
            artists = c
    if isinstance(after.activity, Spotify):
        if isinstance(before.activity, Spotify):
            for artist in before.activity.artists:
                fixed = list(artist.lower())
                if artist not in after.activity.artists:
                    channels = client.guilds[0].text_channels
                    for c in channels:
                        for i in range(len(fixed)):
                            if not fixed[i].isalnum() and fixed[i] != ' ':
                                fixed[i] = ''
                        if c.name == '-'.join(''.join(fixed).split()):
                            temp = c                       
                    overwrite = discord.PermissionOverwrite()
                    overwrite.send_messages = False
                    overwrite.read_messages = False
                    await temp.set_permissions(member, overwrite=overwrite)
                    if len(temp.members) == 2:
                        await temp.delete()
        for artist in after.activity.artists:
            v = False
            fixed = list(artist.lower())
            for i in range(len(fixed)):
                if not fixed[i].isalnum() and fixed[i] != ' ':
                    fixed[i] = ''
            g = '-'.join(''.join(fixed).split())
            for c in client.guilds[0].text_channels:
                if c.name == g:
                    v = True
                    chan = c
            if v:
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = True
                overwrite.read_messages = True
                await chan.set_permissions(member, overwrite=overwrite)
            else:
                overwrites = {client.guilds[0].default_role: discord.PermissionOverwrite(read_messages=False), client.guilds[0].me: discord.PermissionOverwrite(read_messages=True), member: discord.PermissionOverwrite(read_messages = True), member: discord.PermissionOverwrite(send_messages = True)}
                await client.guilds[0].create_text_channel(name = g, overwrites = overwrites, category = artists, nsfw = False)
    elif isinstance(before.activity, Spotify):
        for artist in before.activity.artists:
            fixed = list(artist.lower())
            channels = client.guilds[0].text_channels
            for c in channels:
                for i in range(len(fixed)):
                    if not fixed[i].isalnum() and fixed[i] != ' ':
                        fixed[i] = ''
                if c.name == '-'.join(''.join(fixed).split()):
                    temp = c
                    overwrite = discord.PermissionOverwrite()
                    overwrite.send_messages = False
                    overwrite.read_messages = False
                    await temp.set_permissions(member, overwrite=overwrite)
                    if len(temp.members) == 2:
                        await temp.delete()

client.run('ODQ0MzI0NDAyNzMyNDY2MTk2.YKQwYA.Qcj3bAPZ8zH3AGNiRUlfgHEOsyk')
