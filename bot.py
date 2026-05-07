import asyncio

import discord
from discord.ext import commands

from config import TOKEN
from data.storage import load_data

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


async def load_extensions():
    await bot.load_extension("commands.admin")
    await bot.load_extension("commands.player")
    await bot.load_extension("commands.prompts")


async def main():
    load_data()

    async with bot:
        await load_extensions()
        await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())