from discord.ext import commands
from util import util
from util import env_exporter
from datetime import datetime, date

admin_role = env_exporter.get_admin_role()


class Util(commands.Cog):

    def __int__(self, bot):
        self.bot = bot

    # This command is very 'dangerous'. You can delete messages you don't want. Be careful
    @commands.command(description='Clears the number of messages given as a parameter\nExample:.clear 2'
                                  '\nReturn:This will erase the last 2 messages')
    @commands.has_role(f'{admin_role}')
    async def clear(self, ctx, amount=0):
        if amount <= 50:
            await ctx.channel.purge(limit=amount + 1)
        else:
            print('You pass the limit of messages')

    @commands.command(
        description='Description: Returns the amount of time left until the given date(birthday) and if the date is '
                    'today, return the message "HAPPY BIRTHDAY"\nStandard that the date needs to be given:'
                    ' "day-month-year"\nExample: 14-03-2024')
    async def date(self, ctx, date_request):
        dt = datetime.strptime(date_request, "%d-%m-%Y")
        parsed_dt = date(dt.year, dt.month, dt.day)
        await ctx.send(f'{util.time_until(parsed_dt)}')


async def setup(bot):
    await bot.add_cog(Util(bot))
