from discord.ext import commands


class Math(commands.Cog):

    def __int__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print('Bot is online.')

    @commands.command(aliases=['calculate'], description='Description: Give a expression and return the result\nExample:.cal 90+2\n'
                                                         'Return: The answer of the expression "90+2" is: 92')
    async def cal(self, ctx, *, ex='No calculate to do'):
        await ctx.send(f'The answer of the expression "{ex}" is: {str(eval(ex))}', mention_author=True)


async def setup(bot):
    await bot.add_cog(Math(bot))
