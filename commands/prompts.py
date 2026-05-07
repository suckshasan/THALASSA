import discord
from discord.ext import commands

from data.storage import characters, active_prompts


async def setup(bot):

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def prompt(ctx, member: discord.Member, *, text):
        player_id = str(member.id)

        if player_id not in characters:
            await ctx.send("That player has no character.")
            return

        active_prompts[player_id] = {
            "text": text,
            "response": None
        }

        dm = await member.create_dm()

        embed = discord.Embed(
            title="THALASSA DECISION",
            description=text,
            color=discord.Color.dark_teal()
        )

        embed.add_field(
            name="Response Options",
            value="Respond with !encourage or !discourage",
            inline=False
        )

        await dm.send(embed=embed)

        await ctx.send(f"Prompt sent to {member.mention}.")


    @bot.command()
    async def encourage(ctx):
        player_id = str(ctx.author.id)

        if player_id not in active_prompts:
            await ctx.send("No active prompt.")
            return

        active_prompts[player_id]["response"] = "encourage"

        await ctx.send("You encouraged the action.")


    @bot.command()
    async def discourage(ctx):
        player_id = str(ctx.author.id)

        if player_id not in active_prompts:
            await ctx.send("No active prompt.")
            return

        active_prompts[player_id]["response"] = "discourage"

        await ctx.send("You discouraged the action.")