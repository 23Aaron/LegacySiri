from discord.ext import commands
import discord, asyncio, logging, json
bot = commands.Bot(command_prefix=('hey siri ', 'Hey Siri ', 'Hey siri ', 'HEY SIRI ', 'hey Siri'), case_insensitive=True)

# Role ID Dictionary
platformDict = {"watchos":586272313239142443, "watchosbeta":586279940480303105}

@bot.event
async def on_ready():
    print("yeet")

@bot.command(pass_context=True)
async def dickmove(ctx):
    await ctx.send("https://i.imgur.com/QVQKp7X.png")

@bot.command(pass_context=True, name='set')
async def create(ctx):
    await ctx.send("Do it yourself, you lazy git.")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def beta(ctx, platform, version, beta, betaversion):

    transformDict = {"db":"Developer Beta", "pb":"Public Beta"}

    if platform.lower() in platformDict:
        role = platformDict[platform.lower()]

    if beta.lower() in transformDict:
        betas = transformDict[beta.lower()]

    platform = capitaliseOS(platform)

    guild = ctx.guild

    roleObj = guild.get_role(role)

    channel = guild.get_channel(585257236503330818)

    await roleObj.edit(mentionable = True)
    await channel.send("{} {} {} {} {} has been released!".format(roleObj.mention, platform, str(version), betas, str(betaversion)))
    await roleObj.edit(mentionable = False)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def update(ctx, platform, version):

    guild = ctx.guild

    platform = platform.lower()

    role = getRoleID(platform)
    
    platform = capitaliseOS(platform)

    roleObj = guild.get_role(role)

    channel = guild.get_channel(585257236503330818)

    await roleObj.edit(mentionable = True)
    await channel.send("{} {} {} has been released!".format(roleObj.mention, platform, str(version)))
    await roleObj.edit(mentionable = False)

@bot.event
async def on_command_error(ctx, error):
    prefix = await bot.get_prefix(ctx.message)
    
    if isinstance(prefix, list):
        for p in prefix:
            if ctx.message.content.find(p) == 0:
                clean_command = ctx.message.content.replace(p, "")
            else:
                pass
    else:
        pass

    print(clean_command)   

    embed = discord.Embed(
        title = "Sorry, I'm not sure what you meant by that.",
        description = "Now searching the web for " + str(clean_command) + "...",
        colour = 0xffffff
    )
    
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=embed)
    else:
        raise error

def getRoleID(platform):
    platformDict = {"watchos":586272313239142443, "watchosbeta":586279940480303105}
    
    if platform.lower() in platformDict:
        return platformDict[platform.lower()]

def capitaliseOS(msg):
    msg = msg.replace("o", "O")
    msg = msg.replace("s", "S")
    msg = msg.replace("beta", "")
    return msg

bot.run("YOUR_TOKEN_HERE") 