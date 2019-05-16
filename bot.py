from discord.ext import commands
import discord, asyncio, logging, json
bot = commands.Bot(command_prefix=('hey siri ', 'Hey Siri ', 'Hey siri ', 'HEY SIRI ', 'hey Siri'), case_insensitive=True)

@bot.event
async def on_ready():
    print("yeet")

@bot.command(pass_context=True)
async def dickmove(ctx):
    await ctx.send("https://i.imgur.com/QVQKp7X.png")

@bot.command(pass_context=True)
async def set(ctx):
    await ctx.send("Do it yourself, you lazy git.")

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


    

bot.run("YOUR_TOKEN_HERE") 