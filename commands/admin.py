from dataclasses import asdict

import discord
from discord.ext import commands

from models.character import Character
from data.storage import characters, active_prompts, save_data


async def setup(bot):

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def addcharacter(
        ctx,
        member: discord.Member,
        character_name: str,
        faction: str,
        district: str,
        *,
        reputation: str
    ):
        character = Character(
            player_id=member.id,
            player_name=member.name,
            character_name=character_name,
            faction=faction,
            district=district,
            reputation=reputation
        )

        characters[str(member.id)] = asdict(character)

        save_data()

        await ctx.send(
            f"Character `{character_name}` assigned to {member.mention}."
        )


    @bot.command()
    @commands.has_permissions(administrator=True)
    async def removecharacter(ctx, member: discord.Member):
        player_id = str(member.id)

        if player_id not in characters:
            await ctx.send("No character found.")
            return

        del characters[player_id]

        if player_id in active_prompts:
            del active_prompts[player_id]

        save_data()

        await ctx.send("Character removed.")


    @bot.command()
    @commands.has_permissions(administrator=True)
    async def listcharacters(ctx):
        if not characters:
            await ctx.send("No characters registered.")
            return

        lines = []

        for char in characters.values():
            lines.append(
                f"{char['character_name']} | {char['faction']} | {char['district']}"
            )

        await ctx.send("\n".join(lines))