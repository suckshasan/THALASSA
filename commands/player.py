import discord

from data.storage import characters


async def setup(bot):

    @bot.command()
    async def me(ctx):
        player_id = str(ctx.author.id)

        if player_id not in characters:
            await ctx.send("You do not have a character.")
            return

        c = characters[player_id]

        embed = discord.Embed(
            title=c["character_name"],
            color=discord.Color.blue()
        )

        embed.add_field(name="Faction", value=c["faction"], inline=True)
        embed.add_field(name="District", value=c["district"], inline=True)
        embed.add_field(name="Stress", value=str(c["stress"]), inline=True)

        await ctx.send(embed=embed)